"""
三大特征 封装  继承  多态
封装(官话)：把对象的状态信息隐藏在对象的内部，
         不允许外部程序直接访问对象的内部信息
         而是通过类提供的方法(公开)来实现对内部信息的操作和访问
好处：向类外提供必要的功能，隐藏了类的内部实现细节
封装主要是通过私有属性和私有方法来实现 名称前面加双下划线 __xxx
实际呢：障眼法 依然能访问

"""


class MyClass:
    def __init__(self, data):
        self.__data = data

    def __fun1(self):
        print("dadada")


m1 = MyClass(111)
# print(m1.data)  # 报错
# print(m1.__fun1)  # 报错
print(m1.__dict__)  # {'_MyClass__data': 111}
print(m1._MyClass__data)  # 111
m1._MyClass__fun1()
