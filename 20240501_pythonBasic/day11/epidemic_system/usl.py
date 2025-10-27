from dtl import EpidemicModel
from bll import EpidemicController


class EpidemicView:
    def __init__(self):
        self.controller = EpidemicController()

    @staticmethod
    def display_menu():
        print("""
            按1键添加疫情信息
            按2键显示疫情信息
            按3键删除疫情信息
            按4键修改疫情信息
            按5键退出系统""")

    def select_menu(self):
        number = input("请输入数字：")
        if number == "1":
            self.input_epidemic()
        elif number == "2":
            self.display_epidemic()
        elif number == "3":
            self.delete_epidemic()
        elif number == "4":
            self.modify_epidemic()
        elif number == "5":
            exit("系统已退出")

    def input_epidemic(self):
        self.controller.add_epidemic(
            EpidemicModel(input("请输入地区名称："),
                          int(input("请输入新增人数：")),
                          int(input("请输入现有人数："))))

    def display_epidemic(self):
        for item in self.controller.epidemic_list:
            print(item)

    def delete_epidemic(self):
        name = input("请输入删除的地区名称：")
        info = self.controller.remove_epidemic(name)
        if info:
            print("删除成功")
        else:
            print("删除失败")

    def modify_epidemic(self):
        name = input("请输入修改的地区名称：")
        info = self.controller.update_epidemic(name)
        if isinstance(info, int):
            self.controller.epidemic_list[info].new = int(input("请输入新增人数："))
            self.controller.epidemic_list[info].now = int(input("请输入现有人数："))
            print("修改成功")
        else:
            print("修改失败")
