import json

from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=2,
    decode_responses=True
)
# 将buyer_tarena1用户购买的9号商品的购买数量进行累加 -- 数量累加业务功能


product_string = redis_conn.hget('buyer_tarena1', 9)

product_item = json.loads(product_string)

product_item['number'] += 1

redis_conn.hset('buyer_tarena1', 9, json.dumps(product_item))
