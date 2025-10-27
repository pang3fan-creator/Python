class EpidemicController:
    def __init__(self):
        self.epidemic_list = []  # type: list[EpidemicModel]

    def add_epidemic(self, epidemic):
        self.epidemic_list.append(epidemic)

    def remove_epidemic(self, name):
        try:
            self.epidemic_list.remove(name)
            return True
        except ValueError:
            return False

    def update_epidemic(self, name):
        try:
            index_element = self.epidemic_list.index(name)
            return index_element
        except:
            return False


class EpidemicModel:
    def __init__(self, name, new, now):
        self.name = name
        self.new = new
        self.now = now

    def __str__(self):
        return f"地区名称：{self.name}，新增人数：{self.new}，现有人数：{self.now}"

    def __eq__(self, other):
        return self.name == other


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
                          int(input("请输入新增人数：")), int(input("请输入现有人数："))))

    def display_epidemic(self):
        for item in self.controller.epidemic_list:
            print(item)

    def delete_epidemic(self):
        name = input("请输入删除的地区名称：")
        info = self.controller.remove_epidemic(name)
        if info:
            print("删除成功")
        else:
            print("删除失败,不存在该地区")

    def modify_epidemic(self):
        name = input("请输入修改的地区名称：")
        info = self.controller.update_epidemic(name)
        if isinstance(info, int):
            self.controller.epidemic_list[info].new = int(input("请输入新增人数："))
            self.controller.epidemic_list[info].now = int(input("请输入现有人数："))
            print("修改成功")
        else:
            print("修改失败")


epidemic_view = EpidemicView()
if __name__ == '__main__':
    while True:
        epidemic_view.display_menu()
        epidemic_view.select_menu()
