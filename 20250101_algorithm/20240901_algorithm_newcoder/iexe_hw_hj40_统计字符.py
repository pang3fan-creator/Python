"""
输入一行字符串，可以有空格
统计其中英文字符，空格字符，数字字符，其他字符的个数
"""

while True:
    try:
        s = input().strip()
        num_e, num_s, num_n, num_o = 0, 0, 0, 0
        for i in s:
            if i.isdigit():  # 数字
                num_n += 1
            elif i.isalpha():  # 字母
                num_e += 1
            elif i.isspace():  # 空格
                num_s += 1
            else:  # 其他
                num_o += 1
        print(f"{num_e}\n{num_s}\n{num_n}\n{num_o}")
    except:
        break
