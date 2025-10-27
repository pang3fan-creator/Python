from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from users.models import UserProfile
from goods.models import SKU
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
        from .models import OrderInfo
        data = json.loads(request.body)
        address_id = data.get('address_id')
        settlement_type = data.get('settlement_type')
        # 获取用户模型实例
        userprofile = UserProfile.objects.get(username=username)

        # 生成订单号
        from datetime import datetime
        from time import time
        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(int(time()))

        # 获取地址信息
        address_object = userprofile.address_set.filter(pk=address_id).first()

        from .models import OrderGoods

        total_count = 0
        total_amount = 0
        # 来自购物车
        if settlement_type == '0':
            # 将缓存中被选定的商品信息写入到订单表及订单信息表
            # 写入订单信息数据

            # 获取出被选定的商品ID列表及计算出销售总量,并且SKU模型来计算数据
            from django_redis import get_redis_connection
            redis_conn = get_redis_connection(alias='carts')
            cache_key = f'buyer_{username}'
            cache_value_dict = redis_conn.hgetall(cache_key)
            for cache_item_key, cache_item_value_string in cache_value_dict.items():
                cache_item_value_dict = json.loads(cache_item_value_string)
                if cache_item_value_dict.get('status'):
                    sku_object = SKU.objects.get(pk=cache_item_key)
                    total_amount += sku_object.price * cache_item_value_dict.get('number')
                    total_count += cache_item_value_dict.get('number')
            OrderInfo.objects.create(
                user_profile=userprofile,
                order_id=order_id,
                total_amount=total_amount,
                total_count=total_count,
                freight=0,
                status=1,
                receiver=address_object.receiver,
                address=address_object.address,
                receiver_mobile=address_object.receiver_mobile,
                tag=address_object.tag
            )
            ###########################################
            # 循环写入订单商品表
            for cache_item_key, cache_item_value_string in cache_value_dict.items():
                cache_item_value_dict = json.loads(cache_item_value_string)
                if cache_item_value_dict.get('status'):
                    sku_object = SKU.objects.get(pk=cache_item_key)
                    OrderGoods.objects.create(
                        # 数据表字段方式赋值
                        order_info_id=order_id,
                        # 模型实例方式赋值
                        sku=sku_object,
                        count=cache_item_value_dict.get('number'),
                        price=sku_object.price
                    )
        # 来自直接购买
        if settlement_type == '1':
            # 直接将提交的数据信息写入到订单表及订单信息表
            total_count = buy_count = data.get('buy_count')
            sku_id = data.get('sku_id')
            # #############################################
            sku_object = SKU.objects.get(pk=sku_id)
            total_amount = int(buy_count) * sku_object.price
            OrderInfo.objects.create(
                user_profile=userprofile,
                order_id=order_id,
                total_amount=total_amount,
                total_count=buy_count,
                freight=0,
                status=0,
                receiver=address_object.receiver,
                address=address_object.address,
                receiver_mobile=address_object.receiver_mobile,
                tag=address_object.tag
            )
            ###############################################
            # 写入订单商品表
            OrderGoods.objects.create(
                # 数据表字段方式赋值
                order_info_id=order_id,
                # 模型实例方式赋值
                sku=sku_object,
                count=buy_count,
                price=sku_object.price
            )

        ################################################################
        # 分别读取应用程序私钥和支付宝公钥
        with open('key_files/app_private_key.pem') as file:
            app_private_key_string = file.read()

        with open('key_files/alipay_public_key.pem') as file:
            alipay_public_key_string = file.read()

        # 支付宝SDK
        from alipay import AliPay

        # Alipay的构造函数
        alipay_object = AliPay(
            appid='9021000128661963',
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
        )
        # 调用支付方法 --  返回最终的订单信息字符串
        query_string = alipay_object.api_alipay_trade_page_pay(
            # 订单标题
            subject='达达商城支付页面',
            # 商户订单号
            out_trade_no=order_id,
            # 订单总金额
            total_amount=float(total_amount),
            # 同步通知地址
            return_url='http://127.0.0.1:7000/dadashop/templates/pay_success.html',
            # 异步通知地址
            notify_url='http://127.0.0.1:7000/dadashop/templates/pay_success.html'
        )
        ################################################################
        context = {
            'code': 200,
            'data': {
                'saller': '达达商城',
                'total_amount': total_amount,  # 总价格
                'order_id': order_id,
                'pay_url': 'https://openapi-sandbox.dl.alipaydev.com/gateway.do?' + query_string,
                'carts_count': total_count  # 所有商品的总量，如1号商品购买了3件，5号商品购买了2件，则该数字为5
            }
        }
        return JsonResponse(context)

    def get(self, request, username):
        type_val = request.GET.get('type')
        # 0代表全部订单
        if type_val == '0':
            pass
        # 1代表待付款
        if type_val == '1':
            pass
        # 2代表待发货
        if type_val == '2':
            pass
        # 3代表待收货
        if type_val == '3':
            pass
        # 4代表已完成
        if type_val == '4':
            pass

        #####################################################################

        if type_val in ['0', '1', '2', '3', '4']:
            # 当前用户的所有订单
            orders_list = []
            # 1.获取当前用户的所有订单
            # 1.1 获取当前用户
            userprofile = UserProfile.objects.get(username=username)
            # 1.2 获取当前用户的所有订单 -- 一对多的反向关系
            if type_val in ['1', '2', '3', '4']:
                orderinfos = userprofile.orderinfo_set.filter(status=type_val)
            else:
                orderinfos = userprofile.orderinfo_set.all()
            # 2.通过遍历当前用户的所有订单，以获取单一订单信息
            for orderinfo in orderinfos:
                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                # 当前订单的所有商品信息
                order_sku = []
                # 从数据模型中获取当前订单的所有商品信息-- 一对多的反向关系
                ordergoods = orderinfo.ordergoods_set.all()
                # 通过循环将当前订单的所有商品信息添加到order_sku列表中
                for ordergood in ordergoods:
                    # 组织单一商品信息()
                    order_sku_item = {
                        # 在订单商品表中只存储了商品的ID，即订单商品表为子表,商品表为父表
                        'id': ordergood.sku.pk,  # 子找父 -- 正向关系
                        'default_image_url': ordergood.sku.default_image_url.name,
                        'name': ordergood.sku.name,
                        'price': ordergood.sku.price,
                        'count': ordergood.j,
                        'total_amount': ordergood.j * ordergood.sku.price,
                        'sku_sale_attr_names': ['尺码', '颜色'],
                        'sku_sale_attr_vals': ['15', '紫色']
                    }
                    # 将商品信息添加到order_sku列表中
                    order_sku.append(order_sku_item)

                # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                # 构一订单的信息结构如下：
                order_item_info = {
                    'order_id': orderinfo.order_id,
                    'order_total_count': orderinfo.total_count,
                    'order_total_amount': orderinfo.total_amount,
                    'order_freight': orderinfo.freight,
                    'status': orderinfo.status,
                    'order_time': orderinfo.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                    # 3.获取当前订单的配送信息(当前的配送信息可直接通过订单信息进行获取)
                    'address': {
                        'title': orderinfo.tag,
                        'address': orderinfo.address,
                        'mobile': orderinfo.receiver_mobile,
                        'receiver': orderinfo.receiver
                    },
                    # 4.获取当前订单的所有商品信息(代码在上面)
                    'order_sku': order_sku
                }
                # 将单一订单信息存入列表
                orders_list.append(order_item_info)
            # print(orders_list)
            ######################################################################

            context = {
                'code': 200,
                'base_url': settings.DADASHOP_MEDIA_URL,
                'data': {
                    #############################
                    # 当前用户的所有订单
                    'orders_list': orders_list
                    ################################
                }
            }

            return JsonResponse(context)

        if type_val == '5':
            order_id = request.GET.get('order_id')
            # 以order_id为条件进行查找，以获取当前订单的总金额、商品总量等信息
            from .models import OrderInfo
            orderinfo = OrderInfo.objects.get(order_id=order_id)
            #######################################################
            # 构建完整的支付宝查询参数信息
            with open('key_files/app_private_key.pem') as file:
                app_private_key_string = file.read()

            with open('key_files/alipay_public_key.pem') as file:
                alipay_public_key_string = file.read()

                # 支付宝SDK
            from alipay import AliPay

            # Alipay的构造函数
            alipay_object = AliPay(
                appid='9021000128661963',
                app_private_key_string=app_private_key_string,
                alipay_public_key_string=alipay_public_key_string,
            )
            # 调用支付方法 --  返回最终的订单信息字符串
            query_string = alipay_object.api_alipay_trade_page_pay(
                # 订单标题
                subject='达达商城支付页面',
                # 商户订单号
                out_trade_no=order_id,
                # 订单总金额
                total_amount=float(orderinfo.total_amount),
                # 同步通知地址
                return_url='http://127.0.0.1:7000/dadashop/templates/pay_success.html',
                # 异步通知地址
                notify_url='http://127.0.0.1:7000/dadashop/templates/pay_success.html'
            )
            #######################################################
            context = {
                'code': 200,
                'data': {
                    # 订单号
                    'order_id': order_id,
                    # 商品的总量
                    'carts_count': orderinfo.total_count,
                    # 总金额
                    'total_amount': orderinfo.total_amount,
                    # 销售方
                    'saller': '达达商城',
                    # 支付地址
                    'pay_url': 'https://openapi-sandbox.dl.alipaydev.com/gateway.do?' + query_string

                }
            }
            return JsonResponse(context)

    def put(self, request, username):
        data = json.loads(request.body)
        order_id = data.get('order_id')
        from .models import OrderInfo
        OrderInfo.objects.filter(order_id=order_id).update(status=4)
        context = {
            'code': 200
        }
        return JsonResponse(context)


def result(request):
    out_trade_no = request.GET.get('out_trade_no')
    total_amount = request.GET.get('total_amount')
    context = {
        'code': 200,
        'data': {
            'order_id': out_trade_no,
            'total_amount': total_amount
        }
    }
    #####################################
    from .models import OrderInfo
    # 将访订单号的状态由1改为2
    OrderInfo.objects.filter(order_id=out_trade_no).update(status=2)
    #####################################
    return JsonResponse(context)


def query(request):
    with open('key_files/app_private_key.pem') as file:
        app_private_key_string = file.read()

    with open('key_files/alipay_public_key.pem') as file:
        alipay_public_key_string = file.read()

        # 支付宝SDK
    from alipay import AliPay

    # Alipay的构造函数
    alipay_object = AliPay(
        appid='9021000128661963',
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
    )

    res = alipay_object.api_alipay_trade_query(trade_no='2024081722001412520503956118')

    print(res)

    return HttpResponse("query")
