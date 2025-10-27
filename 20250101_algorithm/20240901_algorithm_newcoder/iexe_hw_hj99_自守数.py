"""
输入描述：
int型整数

输出描述：
n以内自守数的数量。
"""
while True:
    try:
        count, n = 0, int(input())
        for i in range(0, n + 1):
            if i ** 2 % 10 ** len(str(i)) == i: count += 1
        print(count)
    except:
        break
