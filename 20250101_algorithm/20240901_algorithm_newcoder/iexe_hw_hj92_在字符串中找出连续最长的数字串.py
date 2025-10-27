def func(s: str):
    res = []
    n = 0  # 记录最长子串的长度值
    longer_detect = False  # 检测到更长的子串时，开启开关
    for i in range(len(s)):
        if s[i - n:i + 1].isdigit():  # 下标i+1控制待检测子串总比最大长度值n加了1格
            res = []  # 有更长的子串时，之前res记录的子串都清空
            n += 1
            longer_detect = True
        elif longer_detect:  # 检测最长数字子串后遇到字母，把刚才的子串加入res
            res.append(s[i - n:i])
            longer_detect = False
        elif s[i - n:i].isdigit():  # 以上只将更长的子串加入res，这里处理子串长度和n相同
            res.append(s[i - n:i])
    if s[-n:].isdigit():  # 若末尾最后还有一个n长度纯数字子串，加入res
        res.append(s[-n:])

    print(''.join(res) + ',' + str(n))


while True:
    try:
        s = input()
        func(s)
    except:
        break
