"""
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
数据输出n行，输出结果为按照字典序排列的字符串，大写字母在小写字母前。
"""
import sys

for line in sys.stdin:
    list_str = [input() for __ in range(int(line))]
    list_str.sort()
    for i in list_str: print(i)
