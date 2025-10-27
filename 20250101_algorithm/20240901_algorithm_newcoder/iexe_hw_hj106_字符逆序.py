"""
输入一个字符串，可以有空格
输出逆序的字符串
"""
import sys

for line in sys.stdin:
    print(line.strip()[::-1],end='')
