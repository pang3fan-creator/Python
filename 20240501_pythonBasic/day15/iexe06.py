"""
生成器应用
"""
list1 = [123, 266, 30, 4, 5, 6, 70, 88, 99, 10]


# 定义函数，在列表中找出大于20的数，并且返回新的数据
def find_odd(list_1: list):
    for index in list_1:
        if index > 20:
            yield index


yield_1 = find_odd(list1)
for item in yield_1:
    print(item)
print(item)
