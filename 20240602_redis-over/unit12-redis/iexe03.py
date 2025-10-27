import json
from redis import Redis

redis_conn = Redis(host='127.0.0.1', port=6379, password=None, decode_responses=True, db=0)

pipe = redis_conn.pipeline()
pipe.hset('buyer_tarena1', 1, '{"number":3,"price":1249.50,"status":false}')
pipe.hset('buyer_tarena1', 2, '{"number":3,"price":1249.50,"status":true}')
pipe.hset('buyer_tarena1', 3, '{"number":3,"price":1249.50,"status":false}')
pipe.hset('buyer_tarena1', 4, '{"number":3,"price":1249.50,"status":true}')
pipe.execute()

product_item = redis_conn.hgetall('buyer_tarena1')
print(product_item)

for k, v in product_item.items():
    a = json.loads(v)  # json.loads()的作用：将json字符串转换成python对象
    if not a['status']:
        a['status'] = True
        redis_conn.hset('buyer_tarena1', k, json.dumps(a))  # json.dumps()的作用：将python对象转换成json字符串

product_item = redis_conn.hgetall('buyer_tarena1')
print(product_item)
