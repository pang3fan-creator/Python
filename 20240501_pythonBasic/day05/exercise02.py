"""
    练习：根据月日，计算这是一年的第几天
    公式：前几个月总天数 + 当月天数
    5月10日
    31 29 31 30 + 10
"""
# 把天数放进元组中，随后取值计算
tuple_day = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份："))
day = int(input("请输入日："))

total_day = sum(tuple_day[:month - 1]) + day
print(total_day)
