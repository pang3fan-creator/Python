"""
需求：
定义函数， 在列表中查找第一个奇数
定义函数， 在列表中查找第一个能够被3或者5整除的数字
使用函数式编程解决
"""
list1 = [43, 54, 54, 56, 65, 67]


# 在列表中查找第一个奇数
def find_odd():
    for item in list1:

        if item % 2:
            return item


# 在列表中查找第一个能够被3或者5整除的数字
def find_single():
    for item in list1:
        if item % 3 == 0 or item % 5 == 0:
            return item


# 分
def condition01(item):
    return item % 2


def condition02(item):
    return item % 3 == 0 or item % 5 == 0


def find_number(condition):
    for item in list1:
        if condition(item):
            return item


print(find_number(condition01))
print(find_number(condition02))
