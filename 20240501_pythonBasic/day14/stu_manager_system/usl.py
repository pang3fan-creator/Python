"""
V层
"""
from bll import StuController
from dtl import StuModel

class StuView:
    """
    学生视图 负责处理学生信息的输入、输出等页面逻辑
    """

    def __init__(self):
        self.__controller = StuController()

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_menu(self):
        number = input("请选择服务数字：")
        if number == "1":
            self.__input_stu()
        elif number == "2":
            self.__display_stu()
        elif number == "3":
            self.__del_stu()
        elif number == "4":
            self.__update_stu()

    def __input_stu(self):
        # 跨类调用 每次都是新的
        model = StuModel(
            input("请输入学生姓名："),
            int(input("请输入学生年龄：")),
            input("请输入学生性别：")
        )
        # 存储数据 每次都是旧的
        # 存储数据 --> C层
        #         --> C层的对象
        #         --> 在V层实例化C层(构造函数(旧)，方法内(新))
        #         --> 导入
        self.__controller.add_stu(model)

    def __display_stu(self):
        for item in self.__controller.list_stu:
            print(vars(item))
            print(item)

    def __update_stu(self):
        name = input("请输入要修改的学生名称：")
        model = StuModel(
            input("请输入学生姓名："),
            int(input("请输入学生年龄：")),
            input("请输入学生性别：")
        )
        if self.__controller.modfiy_stu(name, model):
            print("橙啦！")
        else:
            print("失败了~")

    def __del_stu(self):
        name = input("请输入要修改的学生名称：")
        if self.__controller.remove_stu(name):
            print("橙啦！")
        else:
            print("失败了~")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
