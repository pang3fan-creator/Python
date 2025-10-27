# 语法：通过参数传递对象
# 语义：老张自己决定使用何种交通工具去东北
# 适应性：每次由调用者决定对象

# 人类
class Person:
    def __init__(self, name=""):
        self.name = name

    def driver(self,vehicle):
        print(f"{self.name}去东北")
        vehicle.run() #拜托调用者，传递一个对象

# 车类
class Car:
    def run(self):
        print(f"行驶嘟嘟嘟嘟~")

# 灰机类
class Airplane:
    def run(self):
        print(f"飞行呼呼呼呼~")


lz = Person("老张")
lz.driver(Car())

ll = Person("老李")
ll.driver(Airplane())

