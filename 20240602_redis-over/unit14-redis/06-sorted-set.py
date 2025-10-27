from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=5,
    decode_responses=True
)

lists = redis_conn.zrange('news_rank',start=0,end=-1,withscores=True)

redis_conn.set()

for item in lists:
    print(item[0],item[1])
