"""
密码要求:

1.长度超过8位

2.包括：大写字母/小写字母/数字/其它符号，以上四种至少三种

3.不能分割出两个相等的长度大于 2 的子串，例如 abcabc 可以分割出两个 abc，不合法，ababa 则无法分割出2个aba。
注：其他符号不含空格或换行

数据范围：输入的字符串长度满足
"""
import string

while True:
    try:
        p_w = input()
        if len(p_w) <= 8:
            print('NG')
            continue

        count = 0
        count += 1 if any(c in string.ascii_uppercase for c in p_w) else 0
        count += 1 if any(c in string.ascii_lowercase for c in p_w) else 0
        count += 1 if any(c in string.digits for c in p_w) else 0
        count += 1 if any(not c.isalnum() and not c.isspace() for c in p_w) else 0
        if count < 3:
            print('NG')
            continue

        count = 0
        for i in range(len(p_w) - 3):
            if p_w.count(p_w[i:i + 3]) > 1:
                count += 1
                break
        print('OK') if count == 0 else print('NG')

    except:
        break
