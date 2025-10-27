"""
父类：动物(吃 方法)
子类：狗(吃，跑 方法)  鸟(吃，飞 方法)
请你写出代码 体会方法复用
"""


class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("pao")


class Bird(Animal):
    def fly(self):
        print("飞")


d1 = Dog()
d1.run()
d1.eat()

# type 检查对象的类型 是否是 一种类型
# 例如：狗对象的类型是动物类型
print(type(d1) == Dog)  # true
print(type(d1) == Animal)  # false

# isinstance 检查对象 是否为一种 类型
# 例如：狗对象 是一种 动物类型
print(isinstance(d1, Dog))  # true
print(isinstance(d1, Animal))  # true
print(isinstance(d1, Bird))  # false
