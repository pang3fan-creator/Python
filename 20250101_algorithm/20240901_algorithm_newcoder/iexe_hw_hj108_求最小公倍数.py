"""
输入两个正整数A和B。
输出A和B的最小公倍数。
"""
import sys


def gcd(a, b):
    """计算两个数的最大公约数（使用欧几里得算法）"""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """计算两个数的最小公倍数"""
    return abs(a * b) // gcd(a, b)


if __name__ == '__main__':
    for line in sys.stdin:
        a, b = line.strip().split(' ')
        a, b = int(a), int(b)
        print(lcm(a, b))
