"""
C层
"""
from dtl import StuModel

class StuController:
    """
    控制器 负责处理学生信息
    """

    def __init__(self):
        self.list_stu = []

    def add_stu(self, model):
        self.list_stu.append(model)

    def modfiy_stu(self, name, model):
        for item in self.list_stu:
            if item.name == name:
                item.__dict__ = model.__dict__
                return True
        return False

    def remove_stu(self, name):
        model = StuModel(name)

        # 第三种：登堂入室
        if model in self.list_stu:
            self.list_stu.remove(model)
            return True
        return False

        # 第二种：渐入佳境 重写思想
        # for i in range(len(self.list_stu)):
        #     # 此处调用__eq__方法 比较内容
        #     # --> model 对象  --> name属性
        #     # --> M层 outher.name
        #     if self.list_stu[i].__eq__(model):
        #         del self.list_stu[i]
        #         return True
        # return False

        # 第一种：原始方案
        # for i in range(len(self.list_stu)):
        #     if self.list_stu[i].name == name:
        #         del self.list_stu[i]
        #         return True
        # return False
