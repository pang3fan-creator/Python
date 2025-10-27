from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
import json
from django_redis import get_redis_connection
from django.conf import settings


class CartsView(View):
    redis_conn = get_redis_connection(alias='carts')

    def post(self, request, username):
        data = json.loads(request.body)
        sku_id = data.get('sku_id')
        count = int(data.get('count'))
        # 连接到Redis
        # 确定缓存中的key
        cache_key = f'buyer_{username}'
        # 如果当前用户没有购买过任何商品，则直接在REDIS中创建哈希并且写入购物信息
        if not self.redis_conn.exists(cache_key):
            value = {
                'number': count,
                'status': True
            }
            self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(value))
        else:
            # 如果用户已经购买过商品，则需要判断是否购买过当前商品，如果没有购买过的话，则在哈希并且写入购物信息添加当前购物信息，如果购买过的话，则直接更新数量
            if not self.redis_conn.hexists(cache_key, sku_id):
                value = {
                    'number': count,
                    'status': True
                }
                self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(value))
            else:
                cache_field_value_string = self.redis_conn.hget(name=cache_key, key=sku_id)
                cache_field_value_dict = json.loads(cache_field_value_string)
                cache_field_value_dict['number'] += count
                self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(cache_field_value_dict))

        context = {
            'code': 200,
            'data': {
                'carts_count': self.redis_conn.hlen(cache_key)
            },
            'base_url': settings.DADASHOP_MEDIA_URL
        }
        return JsonResponse(context)

    def get(self, request, username):

        data = self.build_data(username)
        # 根据当前用户已购买的商品组织数据
        context = {
            'code': 200,
            'data': data,
            'base_url': settings.DADASHOP_MEDIA_URL
        }

        return JsonResponse(context)

    def delete(self, request, username):
        data = json.loads(request.body)
        sku_id = data.get('sku_id')

        cache_key = f'buyer_{username}'
        self.redis_conn.hdel(cache_key, sku_id)
        context = {
            'code': 200,
            'data': {
                'carts_count': self.redis_conn.hlen(cache_key)
            },
            'base_url': settings.DADASHOP_MEDIA_URL
        }
        return JsonResponse(context)

    def put(self, request, username):

        data = json.loads(request.body)
        state = data.get('state')
        sku_id = data.get('sku_id')
        cache_key = f'buyer_{username}'
        if state == 'add' or state == 'del':
            cache_value_string = self.redis_conn.hget(name=cache_key, key=sku_id)
            cache_value_dict = json.loads(cache_value_string)
            cache_value_dict['number'] += 1 if state == 'add' else -1
            self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(cache_value_dict))
        if state == 'select' or state == 'unselect':
            cache_value_string = self.redis_conn.hget(name=cache_key, key=sku_id)
            cache_value_dict = json.loads(cache_value_string)
            cache_value_dict['status'] = state == 'select'
            self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(cache_value_dict))
        if state == 'selectall' or state == 'unselectall':
            cache_value_dict = self.redis_conn.hgetall(cache_key)
            for cache_field, cache_value_string in cache_value_dict.items():
                cache_value_dict = json.loads(cache_value_string)
                cache_value_dict['status'] = state == 'selectall'
                self.redis_conn.hset(name=cache_key, key=cache_field, value=json.dumps(cache_value_dict))

        '''
        if state == 'add':
            cache_value_string = self.redis_conn.hget(name=cache_key, key=sku_id)
            cache_value_dict = json.loads(cache_value_string)
            cache_value_dict['number'] += 1
            self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(cache_value_dict))
        if state == 'del':
            cache_value_string = self.redis_conn.hget(name=cache_key, key=sku_id)
            cache_value_dict = json.loads(cache_value_string)
            cache_value_dict['number'] -= 1
            self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(cache_value_dict))
        if state == 'select':
            cache_value_string = self.redis_conn.hget(name=cache_key, key=sku_id)
            cache_value_dict = json.loads(cache_value_string)
            cache_value_dict['status'] = True
            self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(cache_value_dict))
        if state == 'unselect':
            cache_value_string = self.redis_conn.hget(name=cache_key, key=sku_id)
            cache_value_dict = json.loads(cache_value_string)
            cache_value_dict['status'] = False
            self.redis_conn.hset(name=cache_key, key=sku_id, value=json.dumps(cache_value_dict))
        if state == 'selectall':
            cache_value_dict = self.redis_conn.hgetall(cache_key)
            for cache_field, cache_value_string in cache_value_dict.items():
                cache_value_dict = json.loads(cache_value_string)
                cache_value_dict['status'] = True
                self.redis_conn.hset(name=cache_key, key=cache_field, value=json.dumps(cache_value_dict))
        if state == 'unselectall':
            cache_value_dict = self.redis_conn.hgetall(cache_key)
            for cache_field, cache_value_string in cache_value_dict.items():
                cache_value_dict = json.loads(cache_value_string)
                cache_value_dict['status'] = False
                self.redis_conn.hset(name=cache_key, key=cache_field, value=json.dumps(cache_value_dict))
        '''
        data = self.build_data(username)
        context = {
            'code': 200,
            'data': data,
            'base_url': settings.DADASHOP_MEDIA_URL
        }
        return JsonResponse(context)


    def build_sku_data(self, sku_list, username, **kwargs):
        from django_redis import get_redis_connection
        redis_conn = get_redis_connection(alias='carts')
        cache_key = f'buyer_{username}'
        from goods.models import SKU, SPUSaleAttr
        data = []
        for id in sku_list:
            # 根据id在数据库查找记录
            sku_object = SKU.objects.get(pk=id)
            # 获取当前商品的属性值
            sku_sale_attr_val = list(sku_object.sale_attr_value.values_list('name', flat=True))
            # 获取当前商品的属性值对应的属性名称
            a = list(sku_object.sale_attr_value.values_list('spu_sale_attr_id', flat=True))
            sku_sale_attr_name = list(SPUSaleAttr.objects.values_list('name', flat=True).filter(pk__in=a))
            ############################################
            # 根据Redis缓存信息来拼接部分数据
            if redis_conn.hexists(cache_key, id):
                cache_value_item_dict = json.loads(redis_conn.hget(name=cache_key, key=id))
                if kwargs.get('buy_num'):
                    number = kwargs.get('buy_num')
                else:
                    number = cache_value_item_dict.get('number')
                status = cache_value_item_dict.get('status')
            else:
                number = kwargs.get('buy_num')
                status = True
            data_item = {
                'count': number,
                'selected': status,
                'id': id,
                'sku_sale_attr_name': sku_sale_attr_name,
                'sku_sale_attr_val': sku_sale_attr_val,
                'name': sku_object.name,
                'price': sku_object.price,
                'default_image_url': sku_object.default_image_url.name
            }
            ############################################
            data.append(data_item)
        return data

    def build_data(self, username):

        # 确定缓存中的key
        cache_key = f'buyer_{username}'
        # 获取当前用户所有的购买商品
        cache_value_dict = self.redis_conn.hgetall(cache_key)
        # 列表用于存储组织完成的数据
        data = []
        #
        from goods.models import SKU, SPUSaleAttr
        for cache_value_key, cache_value_item_string in cache_value_dict.items():
            ############################################
            # 根据Redis缓存数据在数据库查找记录
            sku_object = SKU.objects.get(pk=cache_value_key)
            # 获取当前商品的属性值
            sku_sale_attr_val = list(sku_object.sale_attr_value.values_list('name', flat=True))
            # 获取当前商品的属性值对应的属性名称
            a = list(sku_object.sale_attr_value.values_list('spu_sale_attr_id', flat=True))
            sku_sale_attr_name = list(SPUSaleAttr.objects.values_list('name', flat=True).filter(pk__in=a))
            ############################################
            # 根据Redis缓存信息来拼接部分数据
            cache_value_item_dict = json.loads(cache_value_item_string)
            data_item = {
                'count': cache_value_item_dict.get('number'),
                'selected': cache_value_item_dict.get('status'),
                'id': cache_value_key,
                'sku_sale_attr_name': sku_sale_attr_name,
                'sku_sale_attr_val': sku_sale_attr_val,
                'name': sku_object.name,
                'price': sku_object.price,
                'default_image_url': sku_object.default_image_url.name
            }
            ############################################
            data.append(data_item)
        return data
