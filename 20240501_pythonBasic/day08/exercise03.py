"""
定义函数， 根据小时，分钟，秒钟计算总秒数
调用： 提供小时 分钟 秒
调用： 提供分钟 秒
调用： 提供小时 秒
调用： 提供分钟

"""


# 1分钟 60秒
# 1小时 3600秒
def calc_sec(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second


# 提供小时 分钟 秒
print(calc_sec(1, 2, 3))
# 提供分钟 秒
print(calc_sec(minute=1, second=2))
# 调用： 提供小时 秒
print(calc_sec(hour=1, second=2))
print(calc_sec(1, second=2))
# 调用： 提供分钟
print(calc_sec(minute=2))
