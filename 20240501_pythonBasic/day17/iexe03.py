"""
编写一个函数，接收一个筛选函数，一个转换函数和一个列表
筛选出列表中的偶数，求平方根，然后返回新的列表
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 写法一
def function_1(func_1, func_2, list):
    list_2 = []
    for i in list:
        if func_1(i):
            list_2.append(func_2(i))

    return list_2


def choose_even(i):
    return i % 2 == 0


list_new = function_1(choose_even, lambda x: x ** 2, list_1)
print(list_new)


# 写法二
def function_2(func_1, func_2):
    a = filter(func_1, list_1)
    b = map(func_2, a)
    return list(b)


list_new = function_2(lambda i: i % 2 == 0, lambda x: x ** 2)
print(list_new)
