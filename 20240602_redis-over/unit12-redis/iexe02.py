import redis as r
import json

redis_conn = r.Redis(host='127.0.0.1',
                     port=6379,
                     db=0,
                     password=None,
                     decode_responses=True)

pipe = redis_conn.pipeline()

pipe.hset('user', 'username', 'rose')
pipe.hset('user', 'age', 18)
pipe.hset('user', 'id', 1000)
pipe.execute()
user_info = redis_conn.hgetall('user')
print(user_info)

pipe.hset('buyer_tarena1', '1', '{"number":3,"price":1249.50,"status":true}')
pipe.hset('buyer_tarena1', '2', '{"number":3,"price":1249.50,"status":true}')
pipe.hset('buyer_tarena1', '3', '{"number":3,"price":1249.50,"status":true}')
pipe.execute()
products = redis_conn.hgetall('buyer_tarena1')
for k, v in products.items():
    print(k, json.loads(v))
