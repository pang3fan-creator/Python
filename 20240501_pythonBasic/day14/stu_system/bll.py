from dtl import StuModel


class StuController:
    """
    学生管理控制器
    """

    def __init__(self):
        self.stu_list = list()  # type:list[StuModel]

    def add_stu(self, model):
        self.stu_list.append(model)

    def delete_stu(self, name):
        try:
            self.stu_list.remove(name)
            return '删除成功'
        except:
            return '删除失败'

    def update_stu(self, name):
        try:
            info_index = self.stu_list.index(name)
            return info_index
        except:
            return False
