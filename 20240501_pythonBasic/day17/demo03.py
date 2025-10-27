"""
需求：
在旧的功能基础上添加新功能，不能改变旧功能

"""

"""
def old_func():
    print('旧')


def new_func():
    print('新')


# 用新功能代替旧功能
old_func = new_func
# 只能执行新的
old_func()
"""


# 有内有外
#   内：内函数包裹新的功能
#   外：外函数存储旧功能

# 内访问外
#   同时处理新旧功能

# 外返回内
#  让后续的逻辑根据需求调用内部函数
def old_func():
    print('旧')


def new_func(func):
    def wrapper():
        print('新')
        func()

    return wrapper

old_func()

old_func = new_func(old_func)
old_func()
