"""
矩形类 表示一个矩形 宽width 高height
get_area() 计算并返回矩形的面积 长 * 宽
get_len() 计算并返回矩形的周长 2 * (长 + 宽)
set_size() 设置宽width 高height
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            print("长和宽必须大于0")
            self.width = 0
            self.height = 0

    def get_area(self):
        return self.width * self.height

    def get_len(self):
        return 2 * (self.width + self.height)

    def set_size(self, width, height):
        if width > 0 and height > 0:
            self.width = width
            self.height = height
        else:
            print("长和宽必须大于0")


r1 = Rectangle(10, 6)
print(r1.get_len())
print(r1.get_area())

r2 = Rectangle(-10, -6)

r1.set_size(5, 7)
print(r1.get_len())
print(r1.get_area())
