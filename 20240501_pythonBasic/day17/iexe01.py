class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return "编号:%d, 名称:%s, 价格:%d" % (self.cid, self.name, self.price)


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 1000),
    Commodity(1002, "倚天剑", 1000),
    Commodity(1003, "金箍棒", 5210),
    Commodity(1004, "口罩", 200),
    Commodity(1005, "酒精", 300)]

# 1. map 映射 # 需求:获取所有商品名字
a = map(lambda item: {item.name: item.price}, list_commodity_infos)
print(list(a))
print(type(a) == map)
# 2. filter 过滤器 # 需求：查找所有单价小于10000的商品
b = filter(lambda item: item.price < 10000, list_commodity_infos)
print(list(b))
print(type(b) == filter)
# 3. max min 最值
print(max(list_commodity_infos, key=lambda item: item.price))
print(min(list_commodity_infos, key=lambda item: item.price))
# 4. sorted # 升序排列 # 降序排列，有返回值
list_commodity_infos.sort(key=lambda item: item.price, reverse=True)
for item in list_commodity_infos:
    print(item)
list_commodity_infos.sort(key=lambda item: item.price)
for item in list_commodity_infos:
    print(item)

# 5. 获取元组中长度最大的列表 ([1,1],[2,2,2],[3,3,3])
list_3 = [1, 1], [2, 2, 2], [3, 3, 3]
print(max(list_3, key=lambda item: len(item)))
print(min(list_3, key=lambda item: len(item)))

a = range(10)
print(type(a))
for i in a:
    print(i)
