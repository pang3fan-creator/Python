"""
计算一个浮点数的立方根，不使用库函数。
保留一位小数。
"""
import sys

for line in sys.stdin:
    num_line = float(line.strip())
    count = 1 if num_line >= 0 else -1
    num_line *= count
    step_be, step_af = 0, 0.1
    while True:
        num_be, num_af = step_be ** 3, step_af ** 3
        if num_be <= num_line <= num_af:
            result = step_be if abs(num_line - num_be) <= abs(num_line - num_af) else step_af
            print(round(result * count, 1))
            break
        else:
            step_be, step_af = step_af, step_af + 0.1
