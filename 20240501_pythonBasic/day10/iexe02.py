"""
创建一个人的类 属性：姓名  性别  年龄  籍贯
类中有一个函数，能够完成自我介绍：我是来自xxx的xxx，性别xxx，年龄xxx
"""


class Person:
    def __init__(self, name, sex, age, origin=None):
        self.name = name
        self.sex = sex
        self.age = age
        self.origin = origin

    # def say(self):
    #     print(f"我是来自{self.origin}的{self.name}，性别{self.sex}，年龄{self.age}")
    def __str__(self):
        return f"我是来自{self.origin}的{self.name}，性别{self.sex}，年龄{self.age}"


# 根据类创建对象的过程--> 实例化
p1 = Person("夜瑾", "男", 18, "黄土高坡1号坡")
p3 = Person("夜瑾", "男", 18, "黄土高坡1号坡")
p2 = Person("小艺", "女", 18, "黄土高坡2号坡")

# 访问  对象.属性
print(p1.origin)
# 修改 对象.属性 = 值
p1.origin = "北京市海淀区万寿路18号院"

# p1.say()
# p2.say()

print(p1)
print(p2)
print(p3)
