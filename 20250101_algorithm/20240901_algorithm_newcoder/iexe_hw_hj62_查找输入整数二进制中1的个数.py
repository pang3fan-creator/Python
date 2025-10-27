"""
输入一个整数
计算整数二进制中1的个数
"""
import sys

for line in sys.stdin:
    line = int(line)
    print(bin(line).count('1'))
