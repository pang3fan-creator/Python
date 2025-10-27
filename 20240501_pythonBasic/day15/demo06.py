"""
内置生成器函数 enumerate 枚举函数
遍历可迭代对象时，可以将索引和元素组成一个元组

for 变量 in enumerate(可迭代对象)
for 索引,元素 in enumerate(可迭代对象)
"""
list1 = [123, 56, 12, 67, 3, 9, 98, 2]
# 读取数据
for item in list1:
    if item > 20:
        print(item)

# 修改数据
for i in range(len(list1)):
    if list1[i] > 20:
        list1[i] = 666
print(list1)

# 读取 + 修改
for i, item in enumerate(list1):
    if item > 20:
        list1[i] = 999
print(list1)
