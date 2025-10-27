from redis import Redis

redis_conn = Redis(host='127.0.0.1',
                   port=6379,
                   password=None,
                   db=5,
                   decode_responses=True)

pipe = redis_conn.pipeline()
pipe.zadd('news_rank', {'news_1': 10, 'news_2': 20, 'news_3': 30})
pipe.execute()

lists = redis_conn.zrange('news_rank', start=0, end=-1, withscores=True)
print(lists)
