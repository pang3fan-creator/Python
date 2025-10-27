import redis as r

redis_conn = r.Redis(host='127.0.0.1', port=6379, db=2, password=None, decode_responses=True)  # 创建Redis连接

keys = redis_conn.keys(pattern='*')  # 获取所有键

for item in keys:
    key_type = redis_conn.type(item)  # 获取键的类型

    if key_type == 'string':
        value = redis_conn.get(item)  # 获取字符串值
    elif key_type == 'list':
        value = redis_conn.lrange(item, 0, -1)  # 获取列表值
    elif key_type == 'set':
        value = redis_conn.smembers(item)  # 获取集合值
    elif key_type == 'zset':
        value = redis_conn.zrange(item, 0, -1, withscores=True)  # 获取有序集合值
    else:
        value = redis_conn.hgetall(item)  # 获取哈希值

    print(f"Key: {item}, Type: {key_type}, Value: {value}, TTL: {redis_conn.ttl(item)}")

for item in keys:
    redis_conn.delete(item)

keys = redis_conn.keys(pattern='*')  # 获取所有键
print(keys)
