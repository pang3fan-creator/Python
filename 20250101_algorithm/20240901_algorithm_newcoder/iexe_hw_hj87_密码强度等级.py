password = input()
sum_1 = 0
digit_sum = 0
alpha_lower = 0
alpha_upper = 0
other = 0
a = 0
b = 0
c = 0
d = 0
e = 0
for x in password:
    if x.isdigit():
        digit_sum += 1
    elif x.isupper():
        alpha_upper += 1
    elif x.islower():
        alpha_lower += 1
    else:
        other += 1
# 计分/长度分
a = len(password)
if a <= 4:
    sum_1 = 5
elif 5 <= a <= 7:
    sum_1 = 10
else:
    sum_1 = 25
# 计分/字母分
if alpha_upper != 0:
    if alpha_lower != 0:
        sum_1 = sum_1 + 20
        a = 1  # 同时含有大小写
    else:
        sum_1 = sum_1 + 10
        b = 1  # 只含有大写
else:
    if alpha_lower != 0:
        sum_1 = sum_1 + 10
        b = 1  # 只含有小写
# 计分/数字分
if digit_sum == 1:
    sum_1 += 10
    d = 1  # 有数字
elif digit_sum > 1:
    sum_1 += 20
    d = 1  # 有数字
# 计分/符号分
if other == 1:
    sum_1 += 10
    e = 1  # 有符号
elif other > 1:
    sum_1 += 25
    e = 1  # 有符号
else:
    e = -1
# 计分/奖励分
if a == 1 and d == 1 and e == 1:
    sum_1 += 5
elif b == 1 and d == 1 and e == 1:
    sum_1 += 3
elif b == 1 and d == 1 and e == -1:
    sum_1 += 2
# 结算
if sum_1 > 90:
    print("VERY_SECURE")
elif sum_1 >= 80:
    print("SECURE")
elif sum_1 >= 70:
    print("VERY_STRONG")
elif sum_1 >= 60:
    print("STRONG")
elif sum_1 >= 50:
    print("AVERAGE")
elif sum_1 >= 25:
    print("WEAK")
elif sum_1 >= 0:
    print("VERY_WEAK")
