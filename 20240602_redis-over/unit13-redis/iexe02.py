import json

from redis import Redis

redis_conn = Redis(host='127.0.0.1',
                   port=6379,
                   password=None,
                   db=2,
                   decode_responses=True)

pipe = redis_conn.pipeline()
pipe.hset('buyer_tarena1', 4, '{"number":3,"price":1249.50,"status":true}')
pipe.hset('buyer_tarena1', 7, '{"number":1,"price":888.88,"status":false}')
pipe.hset('buyer_tarena1', 8, '{"number":1,"price":888.88,"status":false}')
pipe.hset('buyer_tarena1', 10, '{"number":1,"price":888.88,"status":false}')
pipe.hset('buyer_tarena1', 11, '{"number":1,"price":888.88,"status":false}')
pipe.execute()

products = redis_conn.hgetall('buyer_tarena1')
for k, v in products.items():
    p = json.loads(v)
    print('商品ID', k, ',购买数量:', p.get('number'), ',单价:', p.get('price'), ',状态:', p.get('status'), ',总价:',
          p.get('number') * p.get('price'))
