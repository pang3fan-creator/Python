"""
输入描述：
输入一个正整数n。

输出描述：
输出一个相加后的整数。
"""
while True:
    try:
        n, sum_res = int(input()), 0
        for i in range(n): sum_res += 2 + i * 3
        print(sum_res)
    except:
        break
