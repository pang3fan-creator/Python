"""
继承
爷爷   -->  爸爸   --> 儿子  --> ....
"""


class Ye:
    def say(self):
        print("我是爷爷")


class Ba(Ye):
    def teach(self):
        print("我是爸爸")


class Son(Ba):
    def study(self):
        print("我是儿子")


# 多重继承
class Son1(Ba, Ye):
    def study(self):
        print("我是Song1")


b1 = Ba()
b1.say()
b1.teach()

s1 = Son()
s1.say()
s1.teach()
s1.study()

s2 = Son1()
s2.say()
s2.teach()
s2.study()
