from django.core.cache import cache
from django.core.cache import caches

# 测试操作Django_redis缓存
# cache == caches['default']

caches['default'].add("redis_cache", "123456")

print(caches['default'].get('redis_cache'))

print(cache.get('redis_cache'))

caches['default'].set('user_info_name', 'Tom')
caches['default'].set('user_info_password', '123456')
caches['default'].set('user_info_age', 22)

print('get_many:', caches['default'].get_many(['user_info_name', 'user_info_password', 'user_info_age']))

caches['default'].incr('user_info_age', 5)

print('age+5:', caches['default'].get('user_info_age'))

caches['default'].decr('user_info_age', 2)

print('age-2', caches['default'].get('user_info_age'))

caches['default'].delete('user_info_password')

print('password value is', caches['default'].get('user_info_password'))

caches['default'].set('users', [1, 2, 3, 4, 5, 6, 7])
