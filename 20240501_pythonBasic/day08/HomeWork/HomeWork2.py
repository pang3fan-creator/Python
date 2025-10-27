"""
餐厅信息管理系统
    定义显示菜单函数
    定义选择菜单函数
    定义添加餐厅(名称,城市,点评人数,人均消费)函数
    定义查看餐厅(名称,城市,点评人数,人均消费)函数
    定义删除餐厅(名称)函数
    定义修改餐厅(名称,城市,点评人数,人均消费)函数
"""


def selest_nem():
    number = input("请输入数字：")
    if number == "1":
        print("定义添加餐厅")
        input_res()
    elif number == "2":
        print("定义查看餐厅")
        display_res()
    elif number == "3":
        print("定义删除餐厅")
        delete_res()
    elif number == "4":
        print("定义修改餐厅")
        modify_res()


def display_nem():
    print("按1键添加餐厅")
    print("按2键查看餐厅")
    print("按3键删除餐厅")
    print("按4键修改餐厅")


def input_res():
    dict_restaurant = {
        "name": input("请输入餐厅名称："),
        "city": input("请输入餐厅所在城市："),
        "remark": int(input("请输入餐厅点评人数：")),
        "money": int(input("请输入人均消费："))}
    list_restaurant.append(dict_restaurant)


def display_res():
    for item in list_restaurant:
        print(f"{item['name']}餐厅在{item['city']}城市，"
              f"点评人数{item['remark']}，"
              f"人均消费是{item['money']}")


def delete_res():
    name = input("请输入要删除的餐厅名字")
    for item in list_restaurant:
        if item["name"] == name:
            list_restaurant.remove(item)


def modify_res():
    name = input("请输入要修改的餐厅：")
    for item in list_restaurant:
        if item["name"] == name:
            item["name"] = input("请输入要修改的餐厅名称：")
            item["city"] = input("请输入要修改的餐厅城市：")
            item["remark"] = int(input("请输入点评人数："))
            item["money"] = int(input("请输入要人均消费："))


list_restaurant = []
while True:
    display_nem()
    selest_nem()
