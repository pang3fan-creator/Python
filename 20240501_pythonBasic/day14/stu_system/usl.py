from bll import StuController
from dtl import StuModel


class StuView:
    """
    学生管理系统视图层
    """
    def __init__(self):
        self.__ctrl = StuController()

    def main(self):
        while True:
            print("按1键添加学生信息")
            print("按2键删除学生信息")
            print("按3键修改学生信息")
            print("按4键查询学生信息")
            print("按5键退出管理系统")
            self.__select_menu()

    def __select_menu(self):
        choice = input("请输入您的选择：")
        if choice == "1":
            self.__add_stu()
        elif choice == "2":
            self.__delete_stu()
        elif choice == "3":
            self.__update_stu()
        elif choice == "4":
            self.__display_stu()
        else:
            exit('已退出管理系统')

    def __add_stu(self):
        model = StuModel(
            name=input("请输入姓名："),
            age=int(input("请输入年龄：")),
            score=float(input("请输入成绩：")))
        self.__ctrl.add_stu(model)

    def __delete_stu(self):
        name = input("请输入要删除的学生姓名：")
        info = self.__ctrl.delete_stu(name)
        print(info)

    def __update_stu(self):
        name = input("请输入要修改的学生姓名：")
        info = self.__ctrl.update_stu(name)
        if isinstance(info, int):
            self.__ctrl.stu_list[info].age = int(input("请输入年龄："))
            self.__ctrl.stu_list[info].score = float(input("请输入成绩："))
            print("修改成功")
        else:
            print("修改失败")

    def __display_stu(self):
        for item in self.__ctrl.stu_list:
            print(item)
