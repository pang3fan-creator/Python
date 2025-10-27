"""
函数式编程 - 应用
适用于：多个函数，主体结构相同，核心算法不同

"""
list1 = [54, 4, 6, 56, 7, 8]


# 1. 定义函数找第一个大于10的元素
def find_gt10():
    for item in list1:
        if item > 10:
            return item


# 2. 定义函数找第一个小于50的元素
def find_lt50():
    for item in list1:
        if item < 50:
            return item


print(find_gt10())
print(find_lt50())


# 1. 定义回调函数 CallBacks： 将不同核心算法单独定义在函数中
# 回调函数：此函数作为一个函数的实参传递，先传递，后在恰当的时候调用

# 2. 定义高阶函数 Higher Order Functions： 通过参数抽象回调函数
# 高阶函数：接收函数作为参数的函数就是高阶函数
# 高阶函数：返回一个函数作为结果的函数就是高阶函数

def condition01(item):
    return item > 10


def condition02(item):
    return item < 50


def find_single(condition):
    # print(condition) 函数的地址
    for item in list1:
        if condition(item):
            return item


print(find_single(condition01))
print(find_single(condition02))
