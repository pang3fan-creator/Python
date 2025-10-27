from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=0,
    decode_responses=True
)
print(redis_conn.keys())
