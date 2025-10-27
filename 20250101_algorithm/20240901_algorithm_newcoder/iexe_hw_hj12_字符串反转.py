# 接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

import sys

for line in sys.stdin:
    str_line = line.strip()[::-1]
    print(str_line)
