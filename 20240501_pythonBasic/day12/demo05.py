"""
继承数据
"""


class Ba:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Son(Ba):
    # 如果子类没有构造函数，则使用父类的构造函数
    # 需要按照要求传参
    # 如果子类有构造函数，则使用自己的构造函数
    def __init__(self, name, age):
        # 调用父类的构造函数
        super().__init__(name, age)
        self.name = name


b1 = Ba("唐僧", 123)
# s1 = Son("wukong", 123)
# print(s1.name)
# print(s1.age)

# s2 = Son("wukong")
# print(s2.name)
# print(s2.age)#报错

s2 = Son("wukong", 123)
print(s2.name)
print(s2.age)
