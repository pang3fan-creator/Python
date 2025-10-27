"""
第一行输入两个整数n和k
第二行输入一个整数数组
从小到大输出最小的k个整数，用空格分开
"""
import sys

for line in sys.stdin:
    a, b = line.strip().split(' ')
    a, b = int(a), int(b)
    list_num = list(map(int, input().strip().split(' ')))[:a]
    list_num.sort()
    print(' '.join(map(str, list_num[:b])))
