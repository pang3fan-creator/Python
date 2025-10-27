"""
函数中创建的变量、形参、函数外创建的变量 作用范围测试
"""

def add(m, n):
    # 函数内部创建的变量是局部(函数内)的，只能在函数内使用，外部使用报错
    # hehe = 666
    data = m + n

    # 函数自己内部的变量可以打印、修改、运算
    m += 100
    print(m)

    # 函数内可以使用函数外声明的变量，
    # 函数调用之前声明的变量能用(能打印，不能运算)，否则不能用
    # test1 -= 111 #报错
    print(test1)
    # print(test2) #报错

    return data


num = 2
test1 = 666

res = add(1, num)
print(res)

test2 = 999

# print(hehe) #外部使用函数内创建的局部变量报错
# print(m,n) #函数的形参相当于函数内部创建的变量
