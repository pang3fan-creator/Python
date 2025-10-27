"""
元组 存储不会变化的多个数据 由一系列变量组成的不可变序列容器
和列表区别:
列表变化，预留空间 存储机制
元组不变化，按需分配 存储机制
元组名 = (元素,...)
"""
list_movie = ["八角笼中", "消失的她"]
tuple_type = ("剧情", "动作", "喜剧")
print(tuple_type[0])
print(tuple_type[:2])

tuple_type += ("科幻", "玄幻")
print(tuple_type)

for item in tuple_type:
    print(item)

# 注意：没有歧义的情况下，可以省略小括号
tuple_type1 = "剧情", "动作", "喜剧"
# 注意：如果只有一个元素，必须加逗号
tuple_type2 = ("剧情",)
# 注意：这样的写法也是元组 数据后面有逗号
tuple_type3 = "剧情",
tuple_type4 = 1, 2,

print(tuple_type1)
print(type(tuple_type4))

# list_movie = ["八角笼中", "消失的她"]
tuple_type = ("剧情", "动作", "喜剧")

# 序列拆包 可迭代对象中的元素解包到一系列的变量中
# 普通用法
a1, b1, c1 = tuple_type
print(a1, b1, c1)  # 剧情 动作 喜剧

# * 拆包 获取序列中的部分元素，把剩余的元素，存储到一个列表中
*a2, b2 = tuple_type
print(a2, b2)  # ['剧情', '动作'] 喜剧

a3, b3, *c3 = tuple_type
print(a3, b3, c3)  # 剧情 动作 ['喜剧']

*a4, = tuple_type
print(a4)

# 列表和元组互转 利用函数
list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)

# 列表转元组
print(type(tuple(list1)))
# 元组转列表
print(type(list(tuple1)))

a5, b5, c5 = "唐三藏"
print(a5, b5, c5)
