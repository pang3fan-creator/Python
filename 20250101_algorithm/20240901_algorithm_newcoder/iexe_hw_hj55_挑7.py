"""
输入算术表达式
计算出结果值
"""
import sys

for line in sys.stdin:
    count = 0
    num_line = int(line)
    for i in range(1, num_line + 1): count = count + 1 if i % 7 == 0 or '7' in str(i) else count
    print(count)
