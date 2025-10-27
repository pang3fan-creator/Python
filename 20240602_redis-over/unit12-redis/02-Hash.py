from redis import Redis
import json

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    decode_responses=True,
    db=2
)
user_info = redis_conn.hgetall('user')
print(user_info)
print(redis_conn.hdel('user', 'id', 'username'))

redis_conn.hset('user', mapping={
    'username': 'rose',
    'age': 16,
    'sex': 1,
    'id': 1000
})
print(redis_conn.hlen('user'))
redis_conn.hset('buyer_tarena1', mapping={
    1: '{"number":3,"price":1249.50,"status":true}',
    2: '{"number":3,"price":1249.50,"status":true}',
    3: '{"number":3,"price":1249.50,"status":true}',
    4: '{"number":3,"price":1249.50,"status":true}', })
product_itme = redis_conn.hgetall('buyer_tarena1')
print(product_itme)
for k, v in product_itme.items():
    print(json.loads(v))
    print(type(json.loads(v)))
