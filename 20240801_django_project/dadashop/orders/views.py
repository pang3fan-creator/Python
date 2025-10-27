import json
import time
import alipay
from django.views import View
from datetime import datetime
from django.db.models import F
from django.conf import settings
from django.http import JsonResponse
from dadashop.utils import jwt_decode
from goods.models import SKU, SPUSaleAttr
from django_redis import get_redis_connection
from users.models import UserProfile, Address
from orders.models import OrderInfo, OrderGoods, STATUS_CHOICES

# print(request.GET)
# print(request.POST)
# print(request.body)
# print(request.headers)
# print(username)


redis_conn = get_redis_connection(alias='carts')


def verify(request, username):
    jwt_token = request.headers.get('Authorization')
    payload = jwt_decode(jwt_token)
    if not payload: return JsonResponse({'code': 10112, 'error': '用户登录数据被篡改'})
    if username != payload['username']: return JsonResponse({'code': 10112, 'error': '用户篡改'})


def make_list(username):
    skus_list = []
    uname_dict = redis_conn.hgetall(username)
    for k, v in uname_dict.items():  # k就是skuid
        sku_info = SKU.objects.all().get(pk=k)

        sku_sale_attr_val = list(sku_info.sale_attr_value.values_list('name', flat=True))
        a = list(sku_info.sale_attr_value.values_list('spu_sale_attr_id', flat=True))
        sku_sale_attr_name = list(SPUSaleAttr.objects.values_list('name', flat=True).filter(pk__in=a))

        product_dict = json.loads(v)
        if product_dict['status']:
            sku_dict = {'id': k, "name": sku_info.name, "price": sku_info.price,
                        "count": product_dict['number'],
                        "selected": 1, "default_image_url": sku_info.default_image_url.name,
                        "sku_sale_attr_name": sku_sale_attr_name,
                        "sku_sale_attr_val": sku_sale_attr_val}
            skus_list.append(sku_dict)
    return skus_list


def advance(request, username):
    if verify(request, username): return verify(request, username)

    settlement_type = request.GET.get('settlement_type')
    user = UserProfile.objects.get(username=username)
    addresses = Address.objects.filter(user_profile=user)
    if not addresses: return JsonResponse({'code': 10000, "error": '地址为空'})
    adderesses_list = list(
        addresses.values('id', 'address', name=F('receiver'), mobile=F('receiver_mobile'),
                         title=F('tag')).order_by('-is_default'))

    if settlement_type == '0':
        context = {'code': 200, 'base_url': settings.DADASHOP_MEDIA_URL,
                   'data': {'addresses': adderesses_list, 'sku_list': make_list(username)}}
        return JsonResponse(context)
    else:
        sku_id = int(request.GET.get('sku_id'))
        buy_num = int(request.GET.get('buy_num'))

        sku_info = SKU.objects.all().get(pk=sku_id)
        sku_sale_attr_val = list(sku_info.sale_attr_value.values_list('name', flat=True))
        a = list(sku_info.sale_attr_value.values_list('spu_sale_attr_id', flat=True))
        sku_sale_attr_name = list(SPUSaleAttr.objects.values_list('name', flat=True).filter(pk__in=a))

        skus_list = [{'id': sku_id, "name": sku_info.name, "price": sku_info.price,
                      "default_image_url": sku_info.default_image_url.name,
                      "sku_sale_attr_name": sku_sale_attr_name,
                      "sku_sale_attr_val": sku_sale_attr_val,
                      'count': buy_num, 'selected': True}]

        context = {'code': 200, 'base_url': settings.DADASHOP_MEDIA_URL,
                   'data': {'addresses': adderesses_list, 'sku_list': skus_list,
                            "buy_count": buy_num, "sku_id": sku_id}}
        return JsonResponse(context)


def ali_pay(order_info):
    with open('key_files/app_private_key.pem') as file:
        app_private_key_string = file.read()
    with open('key_files/alipay_public_key.pem') as file:
        alipay_public_key_string = file.read()
    alipay_object = alipay.AliPay(
        appid='9021000140608573',
        app_notify_url='http://127.0.0.1:7000/templates/pay_success.html',
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string, )
    query_string = alipay_object.api_alipay_trade_page_pay(
        subject='达达商城支付页面',
        out_trade_no=order_info.order_id,
        total_amount=float(order_info.total_amount),
        return_url='http://127.0.0.1:7000/templates/pay_success.html',
        notify_url='http://127.0.0.1:7000/templates/pay_success.html')
    return f'https://openapi-sandbox.dl.alipaydev.com/gateway.do?{query_string}'


class OrdersView(View):

    def post(self, request, username):
        if verify(request, username): return verify(request, username)
        data = json.loads(request.body)
        address_id = data.get('address_id')
        settlement_type = data.get('settlement_type')

        if settlement_type == '0':
            uname_dict = {int(k): int(json.loads(v)['number']) for k, v in
                          redis_conn.hgetall(username).items() if json.loads(v)['status']}
        else:
            uname_dict = {int(data.get('sku_id')): int(data.get('buy_count'))}

        return self.MySQLModel(username, address_id, uname_dict)

    def get(self, request, username):

        user_profile = UserProfile.objects.filter(username=username).first()
        order_infos = OrderInfo.objects.filter(user_profile=user_profile)
        type_num = int(request.GET.get('type'))

        if type_num == 5:
            order_id = request.GET.get('order_id')
            order_info = OrderInfo.objects.get(order_id=order_id)

            data = {'order_id': order_info.order_id,
                    'carts_count': order_info.total_count,
                    'total_amount': order_info.total_amount,
                    'saller': '达达商城',
                    'pay_url': ali_pay(order_info), }

            contex = {'code': 200, 'data': data}
            return JsonResponse(contex)

        order_info = order_infos.filter(status=type_num) if type_num in (1, 2, 3, 4) else order_infos

        if verify(request, username): return verify(request, username)
        if not order_info: return JsonResponse({'code': 10000, 'error': '空的'})

        orders_list = []
        for item in order_info:
            ordergoods = OrderGoods.objects.filter(order_info=item)
            orders_list_dict_sku = []
            for i in ordergoods:
                sku_sale_attr_val = list(
                    i.sku.sale_attr_value.values_list('name', flat=True))
                a = list(
                    i.sku.sale_attr_value.values_list('spu_sale_attr_id', flat=True))
                sku_sale_attr_name = list(
                    SPUSaleAttr.objects.values_list('name', flat=True).filter(pk__in=a))
                order_list_dict_sku_dict = {
                    "id": i.sku.pk, "total_amount": i.price * i.j,
                    "default_image_url": i.sku.default_image_url.name,
                    "name": i.sku.name, "price": i.price, "count": i.j,
                    "sku_sale_attr_names": sku_sale_attr_name,
                    "sku_sale_attr_vals": sku_sale_attr_val}
                orders_list_dict_sku.append(order_list_dict_sku_dict)
            orders_list_dict = {
                "order_id": item.order_id, "order_total_count": item.total_count,
                "order_total_amount": item.total_amount, "status": item.status,
                "order_freight": item.freight,
                "address": {"title": item.tag, "address": item.address,
                            "mobile": item.receiver_mobile, "receiver": item.receiver},
                "order_sku": orders_list_dict_sku,
                "order_time": item.created_time.strftime('%Y-%m-%d')}
            orders_list.append(orders_list_dict)

        context = {'code': 200, 'data': {"orders_list": orders_list},
                   "base_url": settings.DADASHOP_MEDIA_URL}

        return JsonResponse(context)

    def put(self, request, username):
        if verify(request, username): return verify(request, username)

        order_id = str(json.loads(request.body).get('order_id'))
        OrderInfo.objects.all().filter(order_id=order_id).update(status=4)
        return JsonResponse({'code': 200})

    def MySQLModel(self, username, address_id, uname_dict):
        user_profile = UserProfile.objects.all().get(username=username)
        address_info = Address.objects.all().get(id=address_id)

        time_stamp = time.time()
        date_time = datetime.now().strftime('%Y%m%d%H%M%S')
        order_id = 'q' + date_time + str(int(time_stamp))

        order_info = OrderInfo.objects.create(
            user_profile=user_profile, order_id=order_id, total_amount=0,
            total_count=0, freight=8.62, status=STATUS_CHOICES[0][0],
            receiver=address_info.receiver, address=address_info.address,
            receiver_mobile=address_info.receiver_mobile, tag=address_info.tag)

        total_count = total_amount = 0
        for k, v in uname_dict.items():
            sku_info = SKU.objects.all().get(id=k)
            total_count += v
            total_amount += v * float(sku_info.price)
            OrderGoods.objects.create(
                order_info=order_info, sku=sku_info, count=v, price=float(sku_info.price))

        OrderInfo.objects.filter(order_id=order_id).update(
            total_count=total_count, total_amount=total_amount)

        context = {'code': 200,
                   'data': {'saller': '达达商城', 'total_amount': total_amount,
                            'order_id': order_id, 'carts_count': total_count,
                            'pay_url': ali_pay(order_info)}}
        # 以后再删除
        # if redis_conn.exists(username): redis_conn.delete(username)
        return JsonResponse(context)


def result(request):
    if not jwt_decode(request): return JsonResponse({'code': 10000, 'error': '校验错误s'})
    out_trade_no = request.GET.get('out_trade_no')
    order_info = OrderInfo.objects.all().filter(order_id=out_trade_no).update(status=2)
    return JsonResponse({'code': 200, 'data':
        {'order_id': order_info.order_id, 'total_amount': order_info.total_amount}})
