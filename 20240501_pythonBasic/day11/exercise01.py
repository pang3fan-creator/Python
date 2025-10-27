"""
创建一个商品类 product 拥有以下属性和方法：
name 商品名   price 商品价格  count 商品数量，默认为1
add_count 增加商品数量
reduce_count 减少商品数量(如果数量不足，则不减少)
get_total 计算商品总价
"""


class Product:
    def __init__(self, name, price, count=1):
        self.name = name
        self.price = price
        self.count = count

    # 增加商品数量
    def add_count(self, amount):
        self.count += amount

    # 减少商品数量(如果数量不足，则不减少)
    def reduce_count(self, amount):
        if self.count >= amount:
            self.count -= amount
        else:
            print("库存不足")

    # 计算商品总价
    def get_total(self):
        return self.price * self.count

apple = Product("苹果", 8, 10)
apple.add_count(5)
print(apple.get_total())
apple.reduce_count(1)
print(apple.count)
