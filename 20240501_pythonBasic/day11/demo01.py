"""
跨类调用
请你使用面向对象的思想来描述：
类要承担某些行为

需求  老张开车去东北 老李 老赵 老杨 ....
类    人     车
函数  驾驶   行驶

class 人类
    def 驾驶

class 车:
    def 行驶

"""


# 第一种:
# 语法：直接创建的对象
# 语义：老张每次都是开新车去东北
# 适应性：每次都是新的

# 人类
class Person:
    def __init__(self, name=""):
        self.name = name

    def driver(self):
        print(f"{self.name}驾驶车去东北")
        # 跨类调用
        car = Car()
        car.run()


# 车类
class Car:
    def run(self):
        print(f"行驶嘟嘟嘟嘟~")


lz = Person("老张")
ll = Person("老李")
lz.driver()
ll.driver()
