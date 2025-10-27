"""
使用闭包模拟以下情景：
在银行开户存入10000
购买xx商品花了xx元
购买xx商品花了xx元
"""


def squire_money(money):
    def inner(commodity, price):
        nonlocal money
        money -= price
        print("购买%s商品花了%d元，还剩下%d元" % (commodity, price, money))

        def inner_1(commodity_1, price_1):
            nonlocal money
            money -= price_1
            print("购买%s商品花了%d元，还剩下%d元" % (commodity_1, price_1, money))

        return inner_1

    return inner


a = squire_money(10000)
a("电脑", 1000)("鼠标", 100)
