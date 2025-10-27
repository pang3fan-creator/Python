"""
作用域 变量起作用的范围
局部作用域Local：函数内
全局作用域Global:模块(.py文件)内部

查找规则：
在访问变量时，先找局部变量，之后是去找全局变量

局部变量：
   定义在函数内部的变量是局部的（形参也是）
   只能在函数内部使用，函数外使用报错
   调用函数时才被创建，函数结束后自动销毁

全局变量：
   定义在函数外，模块内部的变量是全局的
   在整个模块（py文件）范围内访问，函数内可以访问，不能直接修改全局变量
"""
# 全局
data1 = 10
data2 = [20]


def fun1():
    # 局部变量
    data3 = 30
    print(data1, data2, data3)


def fun2():
    # data3 报错
    # print(data1, data2, data3)
    pass


def fun3():
    # 函数内声明的局部变量
    data2 = 999

    # global 关键字 变成全局变量
    global data1
    data1 = 666

    print(data1, data2)


def fun4():
    # 修改了全局变量中的指向 原来指向 20  现在 999
    data2[0] = 999

    # global 关键字 变成全局变量
    global data4
    data4 = 777

fun1()
fun2()
fun3()
print(data1, data2)
fun4()
print(data1, data2)
print(data4)
