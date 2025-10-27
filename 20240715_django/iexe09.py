import django
from django.conf import settings
from django_redis import get_redis_connection

# 配置 Django 设置
settings.configure(
    CACHES={
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',  # 根据你的 Redis 配置修改
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                "CONNECTION_POOL_KWARGS": {
                    "decode_responses": True
                }
            },
        }
    }
)

# 初始化 Django
django.setup()

redis_conn = get_redis_connection(alias='default')  # 使用别名 'default'
redis_conn.set("abcdef", "123456", ex=300)

print(redis_conn.get("abcdef"))
print(redis_conn.ttl("abcdef"))


# res = redis_conn.keys(pattern="*")
# print(res)
# for item in res:
#     redis_conn.delete(item)
