"""
声明一个函数接收一个列表作为实参，
删除列表中的奇数
函数内部使用列表推导式完成相关功能
"""

list_new = []


def delOdd(list1):
    # for item in list1[:]:
    #     if item % 2 != 0:
    #         list1.remove(item)
    # return list1
    list_new[:] = [item for item in list1 if item % 2 == 0]


list1 = [2, 4, 3, 11, 76, 19]
# print(delOdd(list1))
res = delOdd(list1)
print(list_new)  # [2, 4,76]
