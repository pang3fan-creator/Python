"""
创建一个疫情类，实例化2个对象并调用函数
属性：地区名称、新增人数、现有人数
调用方法打印当前疫情信息：
    xx地区，今日新增xxx人，现有xx人，共计(新增+现有)xx人

"""


class Epidemic:
    def __init__(self, name, new=0, now=0):
        print("__init__中：", self)
        self.name = name
        self.new = new
        self.now = now

    def display(self):
        # self是调用此方法的对象(谁调用我，self就是谁)
        print("函数中：", self)
        print(f"{self.name}地区，今日新增{self.new}人，"
              f"现有{self.now}人，"
              f"共计{self.new + self.now}人")


e1 = Epidemic("北京", 1, 2)
e2 = Epidemic("天津", 2, 4)
e1.display()
# 为什么本行代码会显示天津的信息呢？
# e2存的是天津相关的信息
e2.display()
print(e1)
