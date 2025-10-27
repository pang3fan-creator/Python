"""
多态 对于一种行为有不同的表现
子类重写父类的方法（在子类中定义和父类相同的方法）

重写内置函数
"""
class Movie:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    # __str__将对象转化成字符串
    def __str__(self):
        return f"电影{self.name}的类型是{self.type}"

    def display(self):
        print(f"电影{self.name}的类型是{self.type}")


m1 = Movie("封神", "剧情")
# <__main__.Movie object at 0x7d673d38c7c0>
print(m1)
print(type(m1))
m1.display()
