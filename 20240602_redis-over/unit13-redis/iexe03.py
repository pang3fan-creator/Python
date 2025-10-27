import json

from redis import Redis

redis_conn = Redis(host='127.0.0.1',
                   port=6379,
                   password=None,
                   db=2,
                   decode_responses=True)

products = redis_conn.hgetall('buyer_tarena1')

for key, json_string in products.items():
    product_item = json.loads(json_string)
    if not product_item.get('status'):
        product_item['status'] = True
        redis_conn.hset('buyer_tarena1', key, json.dumps(product_item))
