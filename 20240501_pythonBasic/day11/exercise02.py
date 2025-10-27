"""
以面向对象的思想 描述下列场景
小明请保洁打扫卫生
小红请保洁打扫卫生
李华请保洁打扫卫生

"""


class Person:
    def __init__(self, name):
        self.name = name
        # 方法2
        # self.obj = Cleaner()

    # def subscribe(self):
    #     print("预约")
    # 方法1
    # obj = Cleaner()
    # obj.clean()
    # 方法2
    # self.obj.clean()

    # 方法3
    def subscribe(self, server):
        print("预约")
        server.clean()


class Cleaner:
    def clean(self):
        print("我扫扫扫！！！")


xm = Person("小明")
# xm.subscribe()
# 方法3
xm.subscribe(Cleaner())
