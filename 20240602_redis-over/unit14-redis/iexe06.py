from redis import Redis
from django_redis.cache import RedisCache
from django_redis.client import DefaultClient

redis_conn = Redis(
    host='127.0.0.1', port=6379,
    password=None, db=4, decode_responses=True)
a = redis_conn.zrange('news_rank', 0, -1)
print(a)
