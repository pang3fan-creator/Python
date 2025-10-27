"""
累加10到60之间的，个位不允许是3、5、8的整数的数字合
"""
sum = 0
for item in range(10, 61):
    # 求个位数
    unit = item % 10

    if unit != 3 and unit != 5 and unit != 8:
        sum += item
print(sum)


sum = 0
for item in range(10, 61):
    # 求个位数
    unit = item % 10
    if unit == 3 or unit == 5 or unit == 8:
        continue

    sum += item
print(sum)