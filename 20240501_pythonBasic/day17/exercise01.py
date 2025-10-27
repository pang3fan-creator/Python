"""
1. 获取所有商品的名称和单价
2. 获取所有单价小于10000的商品信息
3. 对商品按照价格降序排列
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"商品id:{self.cid},商品名称:{self.name},商品单价:{self.price}"


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
# 1. 获取所有商品的名称和单价
print(list(map(lambda c: (c.name, c.price), list_commodity_infos)))

# 2. 获取所有单价小于10000的商品信息
for item in filter(lambda c: c.price < 10000, list_commodity_infos):
    print(item)

# 3. 对商品按照价格降序排列
list_commodity_infos.sort(key=lambda c: c.price, reverse=True)
for item in list_commodity_infos:
    print(item)
