"""
M层
"""


class StuModel:
    """
    模型 负责封装学生数据
    """

    def __init__(self, name="", age="18", sex="男"):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"学生的姓名是：{self.name}，性别为：{self.sex}，年龄：{self.age}"

    def __eq__(self, other):
        return self.name == other.name
