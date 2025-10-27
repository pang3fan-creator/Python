from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=2,
    decode_responses=True
)
# 将buyer_tarena1用户购买的9号商品的删除 -- 删除业务功能

if redis_conn.hexists('buyer_tarena1', 9):
    redis_conn.hdel('buyer_tarena1', 9)
    print('Field removed successful')
else:
    print('Field do not exists')
