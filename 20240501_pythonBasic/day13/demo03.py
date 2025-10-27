"""
重写 __eq__
"""


class Person:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    # __eq__ 相等 __gt__ >
    def __eq__(self, other):
        # 重写了方法按照姓名比较
        return self.name == other.name


p1 = Person("老张", 18)
p2 = Person("老li", 19)
p3 = Person("老li", 19)
# 默认比较的地址
print(p1 == p2)
print(p2 == p3)

list1 = [
    Person("老王"),
    Person("老赵"),
    Person("老吴")
]
# 依次比较数据
# for item in list1:
#     print(item == Person("老赵"))

# in的内部在循环调用 __eq__
print(Person("老赵") in list1)
