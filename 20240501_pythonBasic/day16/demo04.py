"""
lambda表达式  匿名函数
变量 = lambda 形参:函数体
lambda能实现的 def都能
lambda函数体只能有一条语句而且还不能是赋值
优点： 简洁表示匿名函数  灵活 函数要求参数为函数时
缺点： 不能复用(但是本身的设计就不是为了复用而设计)
"""


# 普通函数没有参数
def fun1():
    print("Hello World")


# lambda表达式 没有参数
fun2 = lambda: print("Hello World")
fun1()
fun2()


# 普通函数有参数
def fun3(p1, p2):
    return p1 > p2


# lambda表达式 有参数
fun4 = lambda p1, p2: p1 > p2
print(fun3(1, 2))
print(fun4(1, 3))

# lambda表达式  无参数 有返回值
fun5 = lambda: "Hello World"
# lambda表达式  有参数 无返回值(打印参数)
fun6 = lambda p1: print(p1)
