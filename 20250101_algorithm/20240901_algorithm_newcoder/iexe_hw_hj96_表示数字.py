"""
将一个字符串中所有的整数前后加上符号“*”，其他字符保持不变。连续的数字视为一个整数。
"""

while True:
    try:
        res, s = '', input()
        for i in range(0, len(s), 1):
            if i == len(s) - 1:
                res = res + s[-1] + '*' if s[-1].isdigit() else res + s[i]
            else:
                res = res + s[i] if s[i].isdigit() == s[i + 1].isdigit() else res + s[i] + '*'
        if res[0].isdigit(): res = '*' + res
        print(res)
    except:
        break
