"""
疫情信息管理系统V2
运行文件后 调用 display_menu() 显示菜单
          1. 添加疫情信息
          2. 显示疫情信息
          3. 删除疫情信息
          4. 修改疫情信息
          5. 退出系统

调用 select_menu() 选择菜单(1 2 3 4 5) 进入相关操作
    按1键 调用 input_epidemic() 添加疫情
         (地区、新增人数、现有)
    按2键 调用 display_epidemic() 显示疫情信息
         (显示全部疫情信息 xx地区，新增xx人...)
    按3键 调用 delete_epidemic() 删除疫情信息
         (输入地区删除此地区疫情信息)
    按4键 调用 modify_epidemic() 修改疫情信息
         (输入地区修改此疫情信息，不允许修改地区名称)

"""
import sys

# 声明创建空列表
list_epidemic = []


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
        sys.exit()


# 新增信息
def input_epidemic():
    dict_epidemic = {
        "name": input("请输入地区名称："),
        "new": int(input("请输入新增人数：")),
        "now": int(input("请输入现有人数："))
    }
    list_epidemic.append(dict_epidemic)


# 显示信息
def display_epidemic():
    for item in list_epidemic:
        print(f"{item['name']}地区新增{item['new']}人，现有{item['now']}人")


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
