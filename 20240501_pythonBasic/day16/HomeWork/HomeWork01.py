"""
    创建函数,获取列表中所有大于等于25的年龄
    创建函数,获取列表中第一个大于等于25的年龄
    list_age = [26,23,20,28,24]


    创建函数,获取列表中所有三个字的姓名
    创建函数,获取列表中第一个三个字的姓名
    list_name = ["悟空","猪八戒","唐三藏","沙僧","小白龙"]
"""
list_age = [26, 23, 20, 28, 24]


def get_age_gt25():
    for item in list_age:
        if item >= 25:
            yield item

for item in get_age_gt25():
    print(item)

res = list(get_age_gt25())
print(res[0])


def get_age_gt25():
    for item in list_age:
        if item >= 25:
            return item


list_name = ["悟空", "猪八戒", "唐三藏", "沙僧", "小白龙"]

def get_name_len3():
    for item in list_name:
        if len(item) == 3:
            return item


def get_name_len3():
    for item in list_name:
        if len(item) == 3:
            yield item
