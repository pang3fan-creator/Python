"""
装饰器
"""


# 装饰器函数
def new_func(func):
    # 多合一
    def wrapper(*args):
        # 一拆多
        res = func(*args)
        print(f"新功能{res}")
        return res

    return wrapper
# 原函数
# 等同于创建了一个和原函数名称相同的变量，关联内嵌函数，调用时执行内嵌函数
@new_func
def func2():
    print(f"旧功能2")
    return "要放学了"

print(func2())
