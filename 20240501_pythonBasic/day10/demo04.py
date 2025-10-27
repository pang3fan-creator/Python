"""
画出以下代码的内存图2
"""


class Movie:
    def __init__(self, name, index=0):
        self.name = name
        self.index = index


m1 = Movie("封神", 100)
m2 = m1
m2.name = "阿凡达"
print(m1.name)

