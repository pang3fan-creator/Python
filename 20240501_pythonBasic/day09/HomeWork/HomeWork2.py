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
# 商品数据
prd_info = {
    101: {"name": "屠龙刀", "price": 100},
    102: {"name": "倚天剑", "price": 100},
    103: {"name": "辟邪剑谱", "price": 5},
    104: {"name": "九阳神功", "price": 50},
    105: {"name": "九阴神功", "price": 200}
}

# 购物车列表
list_cart = []


# 购物,运行此方法选择服务
def shopping():
    while True:
        item = input("请输入服务：按1键购买，2键结算，3键退出系统:")
        if item == "1":
            print("进入购买环节~")
            # 调用购买方法
            buying()
        elif item == "2":
            print("进入结算环节~")
            # 调用结算方法
            settlement()
        elif item == "3":
            print("退出系统~")
            break
        else:
            print("目前只有3种服务，请重新输入")


# 结算，运行此方法打印购物车商品信息，结算操作（计算总价）
def settlement():
    print("结算方法触发~")
    # 先打印购物车信息
    print_cart_info()
    # 然后计算购物车中商品总价格
    total = calc_cart_total()
    # 最后完成结算
    paying(total)


# 运行此方法打印购物车商品信息
def print_cart_info():
    print("打印购物车商品信息方法触发~")

    for item in list_cart:
        # print(item)  # {'pid': 101, 'count': 10}
        # 因为购物车中的商品的pid = 商品字典中的商品pid ==> item["pid"] -->101
        # 在根据pid获取商品信息 ==> prd_info[item["pid"]] --> 商品信息
        prd_item = prd_info[item["pid"]]
        # print(prd_item)  # {'name': '屠龙刀', 'price': 100}

        print(f"商品名称:{prd_item['name']},单价:{prd_item['price']},数量:{item['count']}")


# 运行此方法结算购物车商品总价
def calc_cart_total():
    total = 0
    for item in list_cart:
        prd_item = prd_info[item["pid"]]
        total += prd_item["price"] * item["count"]

    return total


# 运行此方法结算操作
def paying(total):
    while True:
        money = float(input(f"总价{total}，请输入金额："))
        if money == total:
            print("钱正好，购买成功，欢迎下次光临~")
            list_cart.clear()
            break
        elif money > total:
            print(f"钱多了，找零{money - total}，欢迎下次光临~")
            list_cart.clear()
            break
        else:
            print(f"钱少了，还差{total - money}，请重新支付~")


# 购买,运行此方法打印商品信息，创建订单
def buying():
    print("购买方法触发~")

    print_prd_info()
    # 第一种方法
    order = create_order()
    list_cart.append(order)
    # 第二种方法
    # create_order()


# 打印商品信息,运行此方法打印商品信息
def print_prd_info():
    print("打印商品信息方法触发~")

    for key, value in prd_info.items():
        print(f"编号{key}，商品是：{value['name']}，单价：{value['price']}")


# 创建订单,运行此方法将商品添加到购物车
def create_order():
    print("创建订单方法触发~")
    # 先输入商品ID，id存在
    pid = get_input_id()
    # 然后输入数量
    count = int(input("请输入购买数量："))

    # 第一种：把订单的信息返回出去，在buy方法中接收,完成添购物车的动作
    order = {"pid": pid, "count": count}
    return order

    # 第二种：直接在本函数中完成
    # list_cart.append({"pid": pid, "count": count})

    print(list_cart)


# 运行此方法可以获取商品编号
def get_input_id():
    while True:
        pid = int(input("请输入商品编号："))
        if pid in prd_info:
            return pid

        print("该商品不存在")


# 调用函数
shopping()
