"""
观察某东首页商品推荐内容， 创建商品类，商品名称 商品价格
创建2个商品对象，在终端中打印商品对象信息： 商品xx，价格为xxx元

如果把车做为一个类，应该有哪些属性?
"""

class Product:
    def __init__(self, name, price):
        # self.变量 = 形参
        # self.title = name # 可行 但会被打死
        self.name = name
        self.price = price


# 变量 = 类名()  类实例化后 --> 对象
p1 = Product("双肩包", 100)
p2 = Product("T恤", 50)

print(p1.name)
print(p2.price)
