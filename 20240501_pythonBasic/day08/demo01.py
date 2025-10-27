"""
函数参数
"""


# 位置参数
# 实参与形参位置一一对应的
def fun1(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


fun1(1, 2, 3)


# TypeError: fun1() missing 1 required positional argument: 'p3'
# fun1(1, 2)
# TypeError: fun1() takes 3 positional arguments but 4 were given
# fun1(1, 2, 3, 4)


# 关键字参数 根据形参的名字进行对应
def fun2(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


fun2(p3=3, p2=2, p1=1)


# fun2(p3=3, p2=2, 1) /#报错位置参数跟随关键字参数

# 序列参数 将一个序列拆分乘多个参数，按照顺序与形参对应
def fun3(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


list1 = [1, 2, 3]
tuple1 = (11, 22, 33)
str1 = "嘿嘿嘿"
dict1 = {
    "cn": 30,
    "ma": 10,
    "en": 20
}
fun3(*list1)
fun3(*tuple1)
fun3(*str1)
fun3(*dict1)  # 得到键
fun3(*dict1.values())  # 得到值
# 我可以不要键名，但是依然要键值，不希望你用values()函数

# 字典实参  利用** 将字典拆解后与形参的名字进行对应
dict2 = {
    "p3": 30,
    "p1": 10,
    "p2": 20
}
fun3(**dict2)


# 命名关键字参数
# p1 是一个位置参数，必须通过位置来提供值
# * 分隔符，表明*号后面的所有参数必须关键字参数
# p2 是一个关键字参数，必须通过名字来提供值
def fun4(p1, *, p2):
    print(p1)
    print(p2)


# fun4(1, 2) #报错，实参多了
fun4(1, p2=5)


# 位置形参 *号元组形参
def fun5(p1, *p2):
    print(p1)
    print(p2)


fun5(1, 2)
fun5(1, 2, 3, 4, 5)


# 位置形参 *号元组形参 命名关键字参数
def fun6(p1, *p2, p3):
    print(p1)
    print(p2)
    print(p3)


fun6(1, 2, p3=3)
fun6(1, 2, 3, 4, 5, p3=3)


# 默认参数 必须从右向左依次存在
def fun7(p1, p2=50, p3=100):
    print(p1)
    print(p2)
    print(p3)


fun7(100)  # 100,50,100
fun7(100, 200)  # 100,200,100
fun7(100, 200, 300)  # 100,200,300
