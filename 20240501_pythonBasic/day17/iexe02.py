"""
1、编写一个函数，接收一个列表，找到列表中大于0的偶数，返回新列表
    list_numbers = [-1, 0, 2, -3, 4, 6, 7, 9, 10]
2、编写一个函数，接收一个税率函数（假设税率5%）和一个商品价格的列表作为参数
    返回一个新列表，其中包含每个商品含税后的价格
    list_prices = [100, 200, 300, 400, 500]
    list_prices = [105, 210, 315, 420, 525]
"""

# 第一个函数
list_numbers = [-1, 0, 2, -3, 4, 6, 7, 9, 10]


def find_even(func):
    for i in list_numbers:
        if func(i):
            yield i


list_new = list(find_even(lambda i: i > 0 and i % 2 == 0))
print(list_new)

list_prices = [100, 200, 300, 400, 500]


# 第一个函数
def find_price_0(tax_rate, list_1: list):
    list_new_1 = []
    for i in list_1:
        list_new_1.append(i * (1+tax_rate))
    return list_new_1


a = find_price_0(0.05, list_prices)
print(a)


# 第二个函数
def find_price_2(tax_rate):
    def tax_price(func):
        for i in list_prices:
            yield func(i, tax_rate)

    return tax_price


price_1 = find_price_2(0.05)
list_new = list(price_1(lambda i, tax_rate: i * (1 + tax_rate)))
print(list_new)


# 第三个函数
def find_price_1(tax_rate):
    def tax_price():
        for i in list_prices:
            yield calculate_price(i, tax_rate)

    def calculate_price(i, j):
        return i * (1 + j)

    return tax_price


price_1 = find_price_1(0.05)
list_new = list(price_1())
print(list_new)
