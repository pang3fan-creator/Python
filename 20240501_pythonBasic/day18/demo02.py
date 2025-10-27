"""
定义一个计算器类
存在4个静态方法，用于执行四则运算
存有1个平方根静态方法，计算数字的平方根 math.sqrt()
外部编写一个测试函数，执行对应的方法，确保程序正常执行带异常处理
"""
import math


class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b

    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("数字不能为负")
        return math.sqrt(a)


def test_calc():
    try:
        Calc.add(2, 3)
        Calc.subtract(5, 2)
        Calc.divide(10, 2)
        Calc.multiply(2, 3)
        Calc.square_root(9)
        Calc.divide(10, 0)
        Calc.square_root(-1)
    except ValueError:
        pass

test_calc()
