"""
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。

例如：

1^3=1

2^3=3+5

3^3=7+9+11

4^3=13+15+17+19

"""
while True:
    try:
        num = int(input())
        num_cube = num ** 3
        num_squre = num ** 2
        str_1 = ''
        for i in range(num): str_1 += str(num_squre - num + 1 + i * 2) + '+'
        print(str_1[:-1])

    except:
        break
