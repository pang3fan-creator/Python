from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from users.models import UserProfile
from django.db.models import F
from carts.views import CartsView
import json
from django.views import View


def advance(request, username):
    #######################################################
    # 方法1：先得到缓存中的所有商品，然后再通过列表推导式过滤下单的商品
    # sku_in_carts = CartsView().build_data(username)
    # sku_in_orders = [item for item in sku_in_carts if item.get('selected')]
    #######################################################
    from django_redis import get_redis_connection
    redis_conn = get_redis_connection(alias='carts')
    cache_key = f'buyer_{username}'
    cache_value_dict = redis_conn.hgetall(name=cache_key)
    sku_list = []
    for cache_item_key, cache_item_value in cache_value_dict.items():
        cache_item_value_dict = json.loads(cache_item_value)
        if cache_item_value_dict.get('status'):
            sku_list.append(cache_item_key)
    # 方法2:通过调用carts模块下的函数来构建数据
    sku_list = CartsView().build_sku_data(sku_list=sku_list, username=username)
    #######################################################

    settlement_type = request.GET.get('settlement_type')
    # 获取用户信息
    userprofile = UserProfile.objects.get(username=username)
    # 获取用户的地址信息
    addresses = list(userprofile.address_set.values('id', 'address', name=F('receiver'), mobile=F('receiver_mobile'),
                                                    title=F('tag')).filter(is_delete=False).order_by('is_default'))
    if settlement_type == '0':
        # 只显示已在购物车且被选定的商品数据

        context = {
            'code': 200,
            'base_url': settings.DADASHOP_MEDIA_URL,
            'data': {
                'addresses': addresses,
                'sku_list': sku_list
            }
        }
        return JsonResponse(context)
    #####################################################
    if settlement_type == '1':
        sku_id = request.GET.get('sku_id')
        buy_num = request.GET.get('buy_num')
        sku_list = CartsView().build_sku_data(sku_list=[sku_id], username=username, buy_num=buy_num)
        context = {
            'code': 200,
            'base_url': settings.DADASHOP_MEDIA_URL,
            'data': {
                'addresses': addresses,
                'sku_list': sku_list,
                'buy_count': buy_num,
                'sku_id': sku_id
            }

        }
        print(context)
        print('立即购买')
        return JsonResponse(context)


class OrdersView(View):
    def post(self, request, username):
        data = json.loads(request.body)
        address_id = data.get('address_id')
        settlement_type = data.get('settlement_type')
        # 订单号的规则： YYYYMMDDHHIISS+时间戳
        # 来自购物车
        if settlement_type == '0':
            # 将缓存中被选定的商品信息写入到订单表及订单信息表
            pass
        # 来自直接购买
        if settlement_type == '1':
            # 直接将提交的数据信息写入到订单表及订单信息表
            pass
        context = {
            'code': 200,
            'data': {
                'saller': '达达商城',
                'total_amount': 1314,#总价格
                'order_id': 2020021601,
                'pay_url': 'http://www.baidu.com',
                'carts_count': 0 # 
            }
        }
        return JsonResponse(context)

    def get(self, request, username):
        return HttpResponse('GET')

    def put(self, request, username):
        return HttpResponse('PUT')
