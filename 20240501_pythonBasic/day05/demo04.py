"""
字典： 由系列 键值对 组成的 可变 散列 容器
键值对  ==> 键名：键值
字典名 = {键名：键值, 键名：键值,...}
"""
# 创建
dict_movie = {
    "name": "八角笼中",
    "actor": "王宝强",
    "type": "剧情",
    "index": 609545
}

# 定位 字典[键]
print(dict_movie["name"])

# 添加 字典[键] = 值
dict_movie["time"] = 2024

# 删除 del 字典[键]
del dict_movie["time"]
print(dict_movie)

# 遍历
# for key in dict_movie:
# print(key)  # 键名
# print(dict_movie[key])

# values() 获取字典中的键值
# for value in dict_movie.values():
#     print(value)

# items() 获取字典中的键 和 键值信息
for key, value in dict_movie.items():
    print(key, value)
