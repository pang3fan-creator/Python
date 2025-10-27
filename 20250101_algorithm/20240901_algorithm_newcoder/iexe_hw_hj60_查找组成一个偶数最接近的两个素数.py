"""
输入一个大于2的偶数
从小到大输出两个素数
"""

import sys


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True


for line in sys.stdin:
    num = int(line)
    for i in range(int(num * 0.5), 1, -1):
        j = num - i
        if is_prime(i) and is_prime(j):
            print(i)
            print(j)
            break
