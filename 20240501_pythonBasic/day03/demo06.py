"""
累加1到100之间的能被3整除的整数合

"""
# 只要是（满足条件）就累加
sum = 0
for item in range(1, 101):
    if item % 3 == 0:
        sum += item
print(sum)

# 只要不是（不满足条件）我就跳过
sum = 0
for item in range(1, 101):
    if item % 3 != 0:
        # 跳出本次循环执行下一次循环
        continue
    sum += item
print(sum)

# a,sum = 1, 0
# while a <= 100:
#     if a % 3 == 0: sum += a
#     a += 1
# print(sum)
