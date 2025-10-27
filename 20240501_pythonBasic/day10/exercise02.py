"""
如果把车做为一个类(抽象)，应该有哪些属性?
品牌brand 车型model 颜色color

实例化得到的对象(具体)
"""


# 汽车类
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


# 创建对象  对象.属性   对象.方法
c1 = Car("BMW", "SUV", "粉色")
c2 = Car("阿斯顿马丁", "轿车", "黑色")

print(f"车辆品牌是：{c1.brand}，车型为：{c1.model}，颜色是：{c1.color}")
print(f"车辆品牌是：{c2.brand}，车型为：{c2.model}，颜色是：{c2.color}")

