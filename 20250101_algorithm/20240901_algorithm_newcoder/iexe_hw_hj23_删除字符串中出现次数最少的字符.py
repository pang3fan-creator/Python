"""
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
删除字符串中出现次数最少的字符后的字符串。
"""
while True:
    try:
        line = input().strip()
        dict_text = {}
        for i in line:
            dict_text.setdefault(i, 0)
            dict_text[i] += 1
        a = sorted(dict_text.items(), key=lambda x: x[1])
        for i, (k, v) in enumerate(a):
            if a[i][1] <= a[0][1]: line = line.replace(k, '')
        print(line)
    except:
        break
