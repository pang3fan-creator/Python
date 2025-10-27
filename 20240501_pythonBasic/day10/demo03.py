"""
画出以下代码的内存图1
"""


class Movie:
    def __init__(self, name, type="", index=0):
        self.name = name
        self.type = type
        self.index = index

    def display(self):
        print(f"电影{self.name}的类型是{self.type},热度是{self.type}")


m1 = Movie("封神", "动作", 100)
m2 = Movie("阿凡达", "科幻")
print(m2.display())
