import json

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django_redis import get_redis_connection

from dadashop.utils import jwt_decode
from goods.models import SKU, SPUSaleAttr

redis_conn = get_redis_connection(alias='carts')


class CartsView(View):
    def verify(self, request, username):
        jwt_token = request.headers.get('Authorization')
        payload = jwt_decode(jwt_token)
        if not payload: return JsonResponse({'code': 10112, 'error': '用户登录数据被篡改'})
        if username != payload['username']: return JsonResponse({'code': 10112, 'error': '用户登录数据被篡改'})

    def make_list(self, username):
        skus_list = []
        uname_dict = redis_conn.hgetall(username)
        for k, v in uname_dict.items():  # k就是skuid
            sku_info = SKU.objects.all().get(pk=k)

            sku_sale_attr_val = list(sku_info.sale_attr_value.values_list('name', flat=True))
            a = list(sku_info.sale_attr_value.values_list('spu_sale_attr_id', flat=True))
            sku_sale_attr_name = list(
                SPUSaleAttr.objects.values_list('name', flat=True).filter(pk__in=a))

            i_info = json.loads(v)
            sku_dict = {
                'id': k, "name": sku_info.name, "price": sku_info.price,
                "count": i_info['number'], "selected": i_info['status'],
                "default_image_url": sku_info.default_image_url.name,
                "sku_sale_attr_name": sku_sale_attr_name,
                "sku_sale_attr_val": sku_sale_attr_val, }
            skus_list.append(sku_dict)
        return skus_list

    def post(self, request, username):
        if self.verify(request, username): return self.verify(request, username)

        sku_id = json.loads(request.body).get('sku_id')
        count = int(json.loads(request.body).get('count'))

        if not redis_conn.hexists(username, sku_id):
            redis_conn.hset(username, sku_id, json.dumps({'number': count, 'status': True}))
        else:
            value_dict = json.loads(redis_conn.hget(username, sku_id))
            value_dict['number'] = int(value_dict['number']) + count
            redis_conn.hset(username, sku_id, json.dumps(value_dict))

        context = {'code': 200, 'base_url': settings.DADASHOP_MEDIA_URL,
                   'data': {'carts_count': redis_conn.hlen(username), }}
        return JsonResponse(context)

    def get(self, request, username):
        if self.verify(request, username): return self.verify(request, username)

        context = {'code': 200, 'data': self.make_list(username), 'base_url': settings.DADASHOP_MEDIA_URL}
        return JsonResponse(context)

    def delete(self, request, username):
        if self.verify(request, username): return self.verify(request, username)
        if not redis_conn.exists(username): return JsonResponse({"code": 30104, "error": '未找到用户'})
        if not redis_conn.hkeys(username): return JsonResponse({"code": 30104, "error": '购物车为空'})

        sku_id = json.loads(request.body).get('sku_id')
        redis_conn.hdel(username, sku_id)
        context = {'code': 200, 'base_url': settings.DADASHOP_MEDIA_URL,
                   'data': {'carts_count': redis_conn.hlen(username), }}
        return JsonResponse(context)

    def put(self, request, username):
        if self.verify(request, username): return self.verify(request, username)
        if not redis_conn.exists(username): return JsonResponse({"code": 30104, "error": '未找到用户'})
        if not redis_conn.hkeys(username): return JsonResponse({"code": 30104, "error": '购物车为空'})

        state = json.loads(request.body).get('state')
        sku_id = json.loads(request.body).get('sku_id')
        uname_dict = redis_conn.hgetall(username)
        if state == 'unselectall' or state == 'selectall':
            for k, v in uname_dict.items():
                i_info = json.loads(v)
                i_info['status'] = state == 'selectall'
                redis_conn.hset(username, k, json.dumps(i_info))
        elif state == 'select' or state == 'unselect':
            i_info = json.loads(redis_conn.hget(username, sku_id))
            i_info['status'] = state == 'select'
            redis_conn.hset(username, sku_id, json.dumps(i_info))
        elif state == 'add' or state == 'del':
            i_info = json.loads(redis_conn.hget(username, sku_id))
            i_info['number'] += 1 if state == 'add' else -1
            if i_info['number'] >= 10: return JsonResponse({"code": 10000, 'error': '超了'})
            if i_info['number'] <= 0: return JsonResponse({"code": 10001, 'error': '最少了，亲'})
            redis_conn.hset(username, sku_id, json.dumps(i_info))

        context = {'code': 200, 'data': self.make_list(username),
                   'base_url': settings.DADASHOP_MEDIA_URL}
        return JsonResponse(context)
