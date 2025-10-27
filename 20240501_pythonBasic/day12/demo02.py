"""
三大特征 封装  继承  多态
面向对象中实现代码复用的一种手段
子类可以继承父类的属性和方法，可以根据自己的需求添加或重写父类的方法
python中通过 class 子类(父类): 这样的方法来表示继承关系

"""


class Father:
    def fsay(self):
        print("我是父类")


class Son(Father):
    def ssay(self):
        print("我是子类")


s1 = Son()
s1.ssay()
s1.fsay()
