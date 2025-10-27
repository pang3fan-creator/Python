"""
容器嵌套
"""
# 字典嵌套元组
dict_movie = {
    "name": "八角笼中",
    "actor": "王宝强",
    "index": 1232,
    "type": ("剧情", "动作")
}
print(dict_movie["type"][1])
# 休息一下 15:20继续
# 列表内嵌套字典
list_movie = [
    {"name": "八角笼中", "index": 10086},
    {"name": "封神第一部", "index": 532622, "type": ("剧情", "动作")}
]
print(list_movie[1]["type"][1])
# 修改八角笼中的index的值+10
list_movie[0]["index"] += 10
# 追加一个电影的信息

list_movie.append({"name":"蜘蛛侠","index":10010})
print(list_movie)
