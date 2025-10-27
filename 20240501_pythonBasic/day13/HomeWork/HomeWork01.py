"""
父类： 车(品牌  颜色 )
子类： 电动车(电池容量，充电功率)
#要求打印子类拥有这些信息： 理想 红色 1000 220
"""


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class EleCar(Car):
    def __init__(self, brand, color, battery, power):
        # 通过super调用父类的构造函数
        super().__init__(brand, color)
        self.battery = battery
        self.power = power


lx = EleCar("理想", "红色", 100000, 220)
print(lx.__dict__)
