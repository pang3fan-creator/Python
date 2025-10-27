# 语法：在构造函数中创建的对象
# 语义：老张每次都是开自己的车去东北
# 适应性：每次都用旧的

# 人类
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def driver(self):
        print(f"{self.name}驾驶车去东北")
        # 对象.属性 对象.方法
        self.car.run()


# 车类
class Car:
    def run(self):
        print(f"行驶嘟嘟嘟嘟~")


lz = Person("老张")
ll = Person("老李")
lz.driver()
ll.driver()
