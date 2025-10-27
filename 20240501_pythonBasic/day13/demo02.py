"""
多态 对于一种行为有不同的表现
子类重写父类的方法（在子类中定义和父类相同的方法）

子类重写父类的方法
老张开车去东北
老张开飞机去东北
父类 Person   run 驾驶方法 驾车去东北

子类 Car      行驶
子类 AirPlane 飞行

"""


class Person:
    def driver(self, vehicle):
        # vehicle是对象
        print(f"{vehicle}去东北")
        # 主要是继承了 Vehicle 就可以
        # 对象关系的判定，判断对象是否为一种类型
        if isinstance(vehicle,Vehicle):
            vehicle.run()

class Vehicle:
    def run(self):
        pass


class Car(Vehicle):

    def run(self):
        print("行驶，嘟嘟嘟嘟")


class AirPlane(Vehicle):
    def run(self):
        print("飞行，呼呼呼呼")

lz = Person()
lz.driver(Car())
lz.driver(AirPlane())
# 这里会报错：因为字符串没有run方法，所以怎么办？
lz.driver("潜水艇")
