"""
电影信息管理系统V1
    运行文件后 显示菜单
              1. 添加电影信息
              2. 显示电影信息
              3. 删除电影信息
              4. 修改电影信息

    选择菜单(1 2 3 4) 进入相关操作
        按1键添加电影
            (电影名称、主演姓名、热搜指数)
        按2键显示电影信息
            (显示全部电影信息，xx的主演是xx，热度是xx)
        按3键删除电影信息
            (输入电影名删除此电影信息)
        按4键修改电影信息
            (输入电影名修改此电影信息，可以修改名称、主演、指数)
"""
# 一定在循环前，如果在循环中，每次都会创建一个新的空列表
list_movie = []
while True:
    # 1.显示菜单
    print("按1键添加电影")
    print("按2键显示电影")
    print("按3键删除电影")
    print("按4键修改电影")

    # 2.选择菜单
    number = input("请输入数字：")
    if number == "1":
        dict_movie = {
            "name": input("请输入电影名称："),
            "actor": input("请输入主演姓名："),
            "index": int(input("请输入热搜指数：")),
        }
        list_movie.append(dict_movie)
        print(list_movie)
    elif number == "2":
        for item in list_movie:
            print(f"{item['name']}的主演是{item['actor']}，热度是{item['index']}")
# 15分钟回来继续 10：10
    elif number == "3":
        name = input("请输入删除的电影名称：")
        for i in range(len(list_movie)):
            if list_movie[i]['name'] == name:
                del list_movie[i]
                break # 报错！
    elif number == "4":
        name = input("请输入修改的电影名称：")
        for item in list_movie:
            if item["name"] == name:
                item["name"] = input("请输入电影名称：")
                item["actor"] = input("请输入演员名称：")
                item["index"] = int(input("请输入新指数："))
