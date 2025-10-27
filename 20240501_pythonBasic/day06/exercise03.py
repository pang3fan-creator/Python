"""
声明计算器函数 calc 此函数含有3个形参 2个数字和1个运算符
函数体内， 利用3个形参完成 四则运算
要求用户自行输入实参值 和 四则运算符号
例如： 用户输入 1  然后输入 +  最后输入 2
      1 + 2 输出3
"""


def calc(num1, f, num2):
    if f == "+":
        print(num1 + num2)
    elif f == "-":
        print(num1 - num2)
    elif f == "*":
        print(num1 * num2)
    elif f == "/":
        if num2 == 0:
            print("除数不能为0")
        else:
            print(num1 / num2)

num1 = float(input("请输入数字1："))
f = input("请输入符号：")
num2 = float(input("请输入数字2："))

calc(num1, f, num2)
