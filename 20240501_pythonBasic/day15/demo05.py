"""
生成器
能够动态（循环一次 计算一次 返回一次）的提供数据的可迭代对象
def 函数名():
    yield 数据
"""


# 包含yield语句的函数，返回值为生成器对象
# yield 产生  生成
def my_range():
    index = 0
    while index < 5:
        yield index
        index += 1

# 调用生成器函数， 就是在创建生成器对象
obj = my_range()
print(obj)

for item in obj:
    print(item)
