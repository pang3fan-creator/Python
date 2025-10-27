"""
使用生成器思想完成
定义一个函数接收一个列表，找出列表中所有的偶数
[44,67,12,88,23,56,19]
"""

# 函数中有yield语句， 就是生成器函数
# 调用生成器函数，就会返回一个生成器对象
# 1. 调用生成器函数会自动创建一个迭代器对象
# 2. 调用迭代器对象的 next()方法时才会执行生成器函数
# 3. 每次执行 yield语句时返回数据

def find_even(data):
    for item in data:
        if item % 2 == 0:
            yield item


list1 = [44, 67, 12, 88, 23, 56, 19]
for item in find_even(list1):
    print(item)
