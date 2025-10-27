from redis import Redis

redis_conn = Redis(host='127.0.0.1',
                   port=6379,
                   password=None,
                   db=0,
                   decode_responses=True)

redis_conn.select(3)

if not redis_conn.exists('users'):
    redis_conn.lpush('users', 'Tom', 'John', 'Rose', 'AID', 'Java')

lists = redis_conn.lrange('users', 0, -1)

for item in lists:
    print(item)
