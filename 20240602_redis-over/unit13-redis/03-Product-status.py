import json

from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=2,
    decode_responses=True
)
# 将buyer_tarena1用户购买的所有商品的状态修改为True -- 全选业务功能


products = redis_conn.hgetall('buyer_tarena1')

for key, json_string in products.items():
    product_item = json.loads(json_string)
    if not product_item.get('status'):
        product_item['status'] = True
        redis_conn.hset('buyer_tarena1', key, json.dumps(product_item))
