"""
输入一个仅包含小写字母的字符串
返回最长回文子串的长度
"""
while True:
    try:
        line = input().strip().lower()
        max_len = 0
        for i in range(len(line)):
            for j in range(i+1, len(line)+1):
                sub_line = line[i:j]
                if sub_line == sub_line[::-1]:
                    max_len = max(max_len, len(sub_line))
        print(max_len)

    except:
        break
