while True:
    try:
        s = str(input().strip())
        jiami = str(input().strip())
        new_key = ''
        for i in s:
            if i.lower() not in new_key:
                new_key += i
        std = 'abcdefghijklmnopqrstuvwxyz'
        old = ''
        for i in std:
            if i not in new_key:
                old += i
        new_s = new_key + old
        dic = {}
        for i, j in zip(std, new_s):
            dic[i] = j
        res = ''
        for i in jiami:
            if i.islower():
                res += dic[i]
            elif i.isupper():
                res += str(dic[o]).upper()
            else:
                res += i
        print(res)
    except:
        break
