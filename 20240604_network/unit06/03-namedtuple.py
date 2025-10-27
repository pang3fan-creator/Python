from collections import namedtuple

# 命名元组是简易版的类,只定义有属性的类,
# 它既有元组的不可变性，又有面向对象访问对象属性的形式
Point = namedtuple('Point', ['x', 'y'])

p = Point(x=2, y=3)

print(p.x)
print(p.y)


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def aa(self):
        return self.x + self.y


a = A(2, 3)
print(a.x)
print(a.y)
print(a.aa())
