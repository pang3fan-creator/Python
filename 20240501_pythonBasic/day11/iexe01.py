class CommodityModel:
    def __init__(self, name, price, count=1):
        self.name = name
        self.unit_price = price
        self.count = count

    def add_count(self, count):
        self.count += count

    def reduce_count(self, count):
        if self.count < count: raise ValueError('库存不足')
        self.count -= count

    def get_total_price(self):
        return self.unit_price * self.count


commodity = CommodityModel('电脑', 10000, 1)
commodity.add_count(15)
commodity.reduce_count(6)
print(f'商品总价：{commodity.get_total_price()}')
