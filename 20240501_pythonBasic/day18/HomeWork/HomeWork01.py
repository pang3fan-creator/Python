"""
   sum_data 原本函数执行  for循环 一边循环一遍加等 xxxx次 sum_data(100) 100次
   为sum_data 增加打印函数， 执行打印时间
   执行的公式： 执行后时间 -  执行前时间
   执行后时间：给原函数扩展了这个功能之后的时间
   执行前时间：直接运行原函数的时间
   start = 现在时间
   执行func()
   stop = 执行后时间
   假设： 执行前时间 00:00:01   执行完代码后  00:00:20
"""

from datetime import datetime


def print_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)  # 调用旧的函数
        stop = datetime.now()
        print(stop - start)
        return res

    return wrapper

@print_time
def sum_data(n):
    sum = 0
    for num in range(n):
        sum += num
    return sum


print(sum_data(10))
print(sum_data(1000000))
