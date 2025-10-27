"""
压岁钱
"""


def get_money(money):
    # print(f"我有{money}元")
    def child_buy(commodity, price):
        # UnboundLocalError: local variable 'money' referenced before assignment
        # nonlocal关键字 允许嵌套函数中修改外层函数的局部变量
        # global money
        nonlocal money
        money -= price
        print(f"买了{commodity}花了{price}钱，还剩下{money}元")

    return child_buy


child_buy = get_money(1000)
child_buy("电子琴", 200)
child_buy("洋娃娃", 100)
