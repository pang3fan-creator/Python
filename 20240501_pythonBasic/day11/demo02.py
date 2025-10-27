# 第二种
class Person:
    def __init__(self, name=""):
        self.name = name

    def driver(self):
        print(f"{self.name}驾驶车去东北")

# 车类
class Car:
    def run(self):
        print(f"行驶嘟嘟嘟嘟~")

lz = Person("老张")
ll = Person("老李")
# 跨类调用 全局
car = Car()
lz.driver()
car.run()
ll.driver()
car.run()