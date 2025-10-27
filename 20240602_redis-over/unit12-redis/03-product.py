from redis import Redis
import json

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    decode_responses=True,
    db=2
)
redis_conn.hset('buyer_tarena1', mapping={
    1: '{"number":3,"price":1249.50,"status":false}',
    2: '{"number":3,"price":1249.50,"status":true}',
    3: '{"number":3,"price":1249.50,"status":false}',
    4: '{"number":3,"price":1249.50,"status":true}', })

product_itme = redis_conn.hgetall('buyer_tarena1')

print(product_itme)
for k, v in product_itme.items():
    a = json.loads(v)
    if a['status'] == 'false':
        a['status'] = 'true'
        redis_conn.hset('buyer_tarena1', k, json.dumps(a))

print(redis_conn.hgetall('buyer_tarena1'))
redis_conn.hdel('buyer_tarena1',4)
print(redis_conn.hgetall('buyer_tarena1'))
redis_conn.delete('buyer_tarena1')
print(redis_conn.hgetall('buyer_tarena1'))
