"""
生成器应用   yield
"""
list1 = [123, 56, 12, 67, 3, 9, 98, 2]


# 定义函数，在列表中找出大于20的值,并返回新的数据
def find_gt20():
    result = []
    for item in list1:
        if item > 20:
            result.append(item)
    return result


print(find_gt20())


# 生成器思维
def find_gt20():
    for item in list1:
        if item > 20:
            yield item


for item in find_gt20():
    print(item)
