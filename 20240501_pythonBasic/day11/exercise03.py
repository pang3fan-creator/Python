"""
疫情信息管理系统V1
   使用的容器嵌套完成对数据的增删改查
疫情信息管理系统V2
   使用函数重构
疫情信息管理系统V3
    使用类和对象代替字典表达疫情

"""
# 声明创建空列表
list_epidemic = []


class Epidemic:
    def __init__(self, name, new=0, now=0):
        self.name = name
        self.new = new
        self.now = now

    def display(self):
        print(f"{self.name}地区新增{self.new}人，现有{self.now}人")


# 显示菜单
def display_menu():
    print("按1键添加疫情信息")
    print("按2键显示疫情信息")
    print("按3键删除疫情信息")
    print("按4键修改疫情信息")
    print("按5键退出系统")


# 选择菜单
def select_menu():
    number = input("请输入数字：")

    if number == "1":
        # 添加信息
        print("添加信息方法触发")
        input_epidemic()
    elif number == "2":
        # 显示信息
        print("显示信息方法触发")
        display_epidemic()
    elif number == "3":
        # 删除信息
        print("删除信息方法触发")
        name = input("请输入删除的地区名称：")
        delete_epidemic(name)
    elif number == "4":
        # 修改信息
        print("修改信息方法触发")
        name = input("请输入修改的地区名称：")
        modify_epidemic(name)
    elif number == "5":
        print("系统已退出")


# 新增信息
def input_epidemic():
    epidemic = Epidemic(
        input("请输入地区名称："),
        int(input("请输入新增人数：")),
        int(input("请输入现有人数："))
    )
    list_epidemic.append(epidemic)


# 显示信息
def display_epidemic():
    for item in list_epidemic:
        item.__display()


# 删除信息
def delete_epidemic(name):
    for item in list_epidemic:
        if item["name"] == name:
            list_epidemic.remove(item)


# 修改信息
def modify_epidemic(name):
    for item in list_epidemic:
        if item["name"] == name:
            item["new"] = int(input("请输入新增人数："))
            item["now"] = int(input("请输入现有人数："))


while True:
    display_menu()
    select_menu()
