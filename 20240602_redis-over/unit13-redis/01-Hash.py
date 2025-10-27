from redis import Redis

redis_conn = Redis(
    host='127.0.0.1',port=6379,
    password=None,db=2,decode_responses=True
)

###################################################

# 设置一个field
redis_conn.hset('user', 'id', 1)

# 设置多个field
redis_conn.hset('user', mapping={
    'username': 'Rose',
    'age': 19,
    'sex': 1,
    'salary': 80000
})

###################################################

# 获取由 field 组成的列表

print(redis_conn.hkeys('user'))

# 获取由 value 组成的列表
print(redis_conn.hvals('user'))

# 删除指定的field
redis_conn.hdel('user', 'id', 'username')

# 获取由field和value组成的字典
user_info = redis_conn.hgetall('user')

for key, value in user_info.items():
    print(key, value)

#########################################################


# 返回哈希中是否存在id的field
print(redis_conn.hexists('user', 'id'))

# 返回哈希中是否存在age的field
print(redis_conn.hexists('user', 'age'))

# 返回哈希中field的数量
print(redis_conn.hlen('user'))

# 返回哈希中age field的累加
print(redis_conn.hincrby('user', 'age'))
