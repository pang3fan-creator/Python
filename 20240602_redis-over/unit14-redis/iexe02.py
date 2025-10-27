from redis import Redis

redis_conn = Redis(host='127.0.0.1',
                   port=6379,
                   password=None,
                   db=0,
                   decode_responses=True)

pipe = redis_conn.pipeline()
pipe.lpush('users', 'Tom')
pipe.lpush('users', 'John')
pipe.lpush('users', 'Rose')
pipe.lpush('users', 'AID')
pipe.lpush('users', 'Java')
pipe.execute()

lists = redis_conn.lrange('users', 0, -1)

for item in lists: print(item)
