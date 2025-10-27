"""
函数式编程 - 入门
"""


def fun1():
    print("fun1")


# 直接调用
fun1()
a = fun1()
print(a)  # None

# 函数地址赋值给了a变量
a = fun1
print(a)  # <function fun1 at 0xxxxxxx>
# 间接调用
a()


def fun2():
    print("fun2")


# 函数中可以调用其他函数
def fun3(fun):
    print("fun3")
    # fun2()  # 固定搭配
    fun()  # 灵活搭配


# 将一个函数作为另外一个函数的实参传递
fun3(fun1)
fun3(fun2)


def fun4(p1, p2):
    p1()
    p2()


fun4(fun1, fun2)
