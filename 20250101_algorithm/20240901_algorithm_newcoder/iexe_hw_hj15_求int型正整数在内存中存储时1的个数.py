"""
输入一个整数（int类型）
这个数转换成2进制后，输出1的个数
"""
import sys

for line in sys.stdin:
    num_line=int(line)
    bin_line=str(bin(num_line))
    print(bin_line.count('1'))

