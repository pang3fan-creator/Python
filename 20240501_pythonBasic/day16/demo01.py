"""
zip
"""
list1 = ["xiaoyi", "xiaoyu", "qincai"]
list2 = [18, 19, 20]

# 可以将多个可迭代对象组合元组
for item in zip(list1, list2):
    print(item)

# 矩阵转置 列变行
list_map = [
    [2, 0, 0, 2],
    [3, 0, 0, 6],
    [5, 1, 2, 9],
    [7, 4, 8, 2],
]
# list_new = []
# for item in zip(list_map[0], list_map[1], list_map[2], list_map[3]):
#     print(item)
#     list_new.append(list(item))
# print(list_new)

# list_new = []
# # 无论你的列表有多少行，通过 * 传递给zip
# for item in zip(*list_map):
#     print(item)
#     list_new.append(list(item))
# print(list_new)

# 列表推导式
list_new = [list(item) for item in zip(*list_map)]
print(list_new)

# 列表推导式   ==> 生成器表达式
# 用推导式形式创建的生成器对象，就是生成器表达式
# 语法： 变量 = (表达式 for 变量 in 可迭代对象 if 条件)
generator_new = (list(item) for item in zip(*list_map))
print(generator_new)
for item in generator_new:
    print(item)
