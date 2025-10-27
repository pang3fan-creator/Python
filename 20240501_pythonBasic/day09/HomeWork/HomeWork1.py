"""
可以不使用函数来完成
1. 老师开了一家超市，有商品 prd_info
2. 用户按1键进行购买，按2键进行结算
3. 如果用户按1键购买内容，需要先列出所有商品：
            格式：编号：101，商品是：屠龙刀，单价：100
      用户输入商品编号进入购买商品环节：
         如果输入的商品编号不存在，则提示商品不存在
         如果输入的商品编号存在，则让用户输入购买数量
            用户输入购买数量后，加入到购物车中
   如果用户按2键则结算购物车
        先展示购物车里的信息：
          商品：屠龙刀，单价：100，数量：10
               倚天剑，单价：100，数量：5
          计算总价：可以显示可不显示
        输入金额：
            总价  1000， 请输入金额
            如果支付金额等于总价，打印：欢迎下次光临
            如果支付金额大于总价，打印：找零xx，欢迎下次光临
            如果支付金额小于总价，打印：金额不足，还差xx
"""
prd_info = {
    101: {"name": "屠龙刀", "price": 100},
    102: {"name": "倚天剑", "price": 100},
    103: {"name": "辟邪剑谱", "price": 5},
    104: {"name": "九阳神功", "price": 50},
    105: {"name": "九阴神功", "price": 200}
}

# 购物车列表
list_cart = []
while True:
    item = input("请输入服务：按1键购买，2键结算:")
    if item == "1":
        print("进入购买环节")
        # 先展示所有商品
        for key, value in prd_info.items():
            print(f"编号{key}，商品是：{value['name']}，单价：{value['price']}")
        # 然后输入商品编号
        while True:
            pid = int(input("请输入商品编号："))

            if pid in prd_info:
                break
            else:
                print("该商品不存在！")
        # 购买数量
        count = int(input("请输入商品购买数量："))
        # 添加购物车
        # 存编号，名称，数量到购物车
        # list_cart.append({"name": prd_info[pid]["name"]})
        # 只存编号和数量
        list_cart.append({"pid": pid, "count": count})
        print("添加购物车")
        print(list_cart)

    elif item == "2":
        print("进入结算环节")
        total = 0

        # [{键:值}]
        for item in list_cart:
            # 知道购物车中商品的pid 和数量 不知道价格
            # 商品字典中知道pid、和商品价格但是不知道数量
            # 商品字典中的pid和购物车字典中的pid一样
            # item["pid"]  ==> 101
            # prd_info[101] ==> {"name": "屠龙刀", "price": 100}
            prd_item = prd_info[item["pid"]]
            total += item["count"] * prd_item["price"]

        while True:
            money = float(input(f"总价{total}，请输入金额："))

            if money == total:
                print("结算成功，欢迎下次光临")
                # 基础款
                # list_cart = []
                # 进阶款 清空列表中的所有元素
                list_cart.clear()
                break
            elif money > total:
                print(f"结算成功，找零{money - total}，欢迎下次光临")
                list_cart.clear()
                break
            else:
                print(f"还差，{total - money}")

    else:
        print("目前只有2种服务，请重新输入")
