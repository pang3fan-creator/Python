from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=0,
    decode_responses=True
)
# 删除buyer_tarena1用户购买的商品 -- 删除业务功能

print(redis_conn.exists('buyer_tarena1'))

redis_conn.delete('buyer_tarena1')

print(redis_conn.exists('buyer_tarena1'))
