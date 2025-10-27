"""
输入一组密码，长度不超过100个字符
输出密码变换后的字符串
"""

import sys

for line in sys.stdin:
    str_new = ""
    for i in line.strip():
        if 65 <= ord(i) < 90:
            str_new += chr(ord(i) + 33)
        elif ord(i) == 90:
            str_new += chr(ord(i) +7)
        elif 97 <= ord(i) < 100:
            str_new += chr(50)
        elif 100 <= ord(i) < 103:
            str_new += chr(51)
        elif 103 <= ord(i) < 106:
            str_new += chr(52)
        elif 106 <= ord(i) < 109:
            str_new += chr(53)
        elif 109 <= ord(i) < 112:
            str_new += chr(54)
        elif 112 <= ord(i) < 116:
            str_new += chr(55)
        elif 116 <= ord(i) < 119:
            str_new += chr(56)
        elif 119 <= ord(i) <= 122:
            str_new += chr(57)
        else:
            str_new += i
    print(str_new)
