"""
封装一个函数，找出列表中所有偶数,并计算偶数的平方，并且返回一个新列表
[1,2,3,4,5,6]  ==> [4,16,36]
"""


def calc_even(list_old):
    # list_new = []
    # for i in list_old:
    #     if i % 2 == 0:
    #         i **= 2
    #         list_new.append(i)
    #
    # return list_new

    # 列表推导式
    return [item ** 2 for item in list_old if item % 2 == 0]


list_old = [1, 2, 3, 4, 5, 6]
print(calc_even(list_old))
