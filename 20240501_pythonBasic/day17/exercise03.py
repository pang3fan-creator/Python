"""
编写一个函数，接受一个筛选函数，一个转换函数和一个列表
筛选出列表中的偶数，求平方，然后返回新的列表
输入：list1 = [1,2,3,4,5,6]  输出：[4,16,36]
"""
filter_func = lambda x: x % 2 == 0
map_func = lambda x: x ** 2


def re_list(filter_func, map_func, lst):
    filter_list = list(filter(filter_func, lst))
    return list(map(map_func, filter_list))


list1 = [1, 2, 3, 4, 5, 6]
res = re_list(filter_func, map_func, list1)
print(res)
