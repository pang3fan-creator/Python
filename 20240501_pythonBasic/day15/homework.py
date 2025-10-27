"""
1. 完成今日练习
2. 完成以下代码（生成器） 
    创建函数,获取列表中所有大于等于25的年龄
    创建函数,获取列表中第一个大于等于25的年龄
    list_age = [26,23,20,28,24]


    创建函数,获取列表中所有三个字的姓名
    创建函数,获取列表中第一个三个字的姓名
    list_name = ["悟空","猪八戒","唐三藏","沙僧","小白龙"]
"""
list_age = [26, 23, 20, 28, 24]

# 利用yield推导式创建生成器
my_age = (index for index in list_age if index >= 25)
print(type(my_age))
for index, value in enumerate(my_age):
    print(f'{index} {value}')


def get_age_1(list_1):
    return (index for index in list_1 if index >= 25)


my_age_1 = get_age_1(list_age)
print(type(my_age_1))
print(next(my_age_1))

list_name = ["悟空", "猪八戒", "唐三藏", "沙僧", "小白龙"]

# 利用yield推导式创建生成器
my_name = (index for index in list_name if len(index) == 3)
print(type(my_name))
for index, value in enumerate(my_name):
    print(f'{index} {value}')


def get_name_1(list_1):
    for index in list_1:
        if len(index) == 3:
            return index


my_name_1 = get_name_1(list_name)
print(type(my_name_1))
print(my_name_1)
