from redis import Redis

redis_conn = Redis(host='127.0.0.1', port=6379, db=0, password=None, decode_responses=True)

keys = redis_conn.keys(pattern='*')
print(keys)

for item in keys:
    print(item, redis_conn.get(item), redis_conn.ttl(item))
    print('--------------------------')

a = redis_conn.set('words', 'byebye')
print(a)
