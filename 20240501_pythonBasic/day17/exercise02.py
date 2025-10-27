"""
1.编写一个函数，接收一个整数列表，找到列表中大于0的偶数，返回新列表
list_numbers = [ 2,0,-1,-6,8,3,7  ]

2.编写一个函数，接收一个税率函数(假设税率5%)和一个商品价格的列表作为参数，
    返回一个新列表，其中包含每个商品含税后的价格
list_price = [100,200,300]
tax_price = [105.0,210.0,315.0]
"""


def con01(num):
    return num > 0 and num % 2 == 0


def find_even(l):
    # return list(filter(con01, l))
    return list(filter(lambda num: num > 0 and num % 2 == 0, l))


list_numbers = [2, 0, -1, -6, 8, 3, 7]
new_list = find_even(list_numbers)
print(new_list)

# 第二题
tax = lambda x: x * 1.05
list_price = [100, 200, 300]

def apply_tax(tan_fun, prices):
    return list(map(tan_fun, prices))

print(apply_tax(tax, list_price))
