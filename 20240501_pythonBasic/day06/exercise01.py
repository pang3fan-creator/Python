"""
疫情信息管理系统V1
    运行文件后 显示菜单
              1. 添加疫情信息
              2. 显示疫情信息
              3. 删除疫情信息
              4. 修改疫情信息
              5. 退出系统
    选择菜单(1 2 3 4 5) 进入相关操作
        按1键添加疫情
            (地区、新增人数、现有、累计)
        按2键显示疫情信息
            (显示全部疫情信息 xx地区，新增xx人...)
        按3键删除疫情信息
            (输入地区删除此地区疫情信息)
        按4键修改疫情信息
            (输入地区修改此疫情信息，不允许修改地区名称)
        按5键退出系统
"""
list_yiqing = []
while True:
    # 1. 显示菜单
    print("按1键添加疫情信息")
    print("按2键显示疫情信息")
    print("按3键删除疫情信息")
    print("按4键修改疫情信息")
    print("按5键退出系统")

    # 2.添加疫情信息
    number = input("请输入数字：")
    if number == "1":
        dict_yiqing = {
            "area": input("请输入疫情地区："),
            "new": int(input("请输入新增人数：")),
            "current": int(input("请输入现有人数：")),
            "total": int(input("请输入累计人数："))
        }

        list_yiqing.append(dict_yiqing)
        print(list_yiqing)
    elif number == "2":
        for item in list_yiqing:
            print(f"{item['area']}地区，新增人数：{item['new']}现有人数：{item['current']}累计人数：{item['total']}")
    elif number == "3":
        name = input("请输入删除的地区：")
        for item in list_yiqing:
            if item["area"] == name:
                list_yiqing.remove(item) #内部有一次查找

        # for i in range(len(list_yiqing)):
        #     if list_yiqing[i]["area"] == name:
        #         del list_yiqing[i]
        #         break
    elif number == '4':
        name = input("请输入地区名称：")
        for item in list_yiqing:
            if item['area'] == name:
                item['new'] = int(input("请输入新的值："))
                item['current'] = int(input("请输入新的值："))
                item['total'] = int(input("请输入新的值："))

    elif number == '5':
        break
