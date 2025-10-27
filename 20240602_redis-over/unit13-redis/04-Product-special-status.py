from redis import Redis
import json

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=2,
    decode_responses=True
)
# 将buyer_tarena1用户购买的9号商品的状态修改为False -- 取消单选的业务功能


product_string = redis_conn.hget('buyer_tarena1',9)

product_item = json.loads(product_string)

product_item['status'] = False

redis_conn.hset('buyer_tarena1',9,json.dumps(product_item))

