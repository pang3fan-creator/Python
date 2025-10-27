from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',
    port=6379,
    password=None,
    db=4,
    decode_responses=True
)

if not redis_conn.exists('programe_language'):
    redis_conn.sadd('programe_language','Javascript','Python','Java','C')

if not redis_conn.exists('backend_language'):
    redis_conn.sadd('backend_language','Python','Java','C++','Go')


count = redis_conn.sinterstore('language','programe_language','backend_language')

# print(count)
# print(type(count))

print(f'交集部分有共同的{count}个成员')

pset = redis_conn.smembers('language')

for item in pset:
    print(item)

