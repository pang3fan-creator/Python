while True:
    try:
        a = input()
        # 构造两个列表，一个列表用来放全字母的字符串2，另外一个列表取出来
        char = []  # 构造一个列表用来存放字符串
        res = [False] * len(a)  # 构造一个列表用来记住非字母的位置
        for i, v in enumerate(a):
            if v.isalpha():  # 如果全是字母则放入char中
                char.append(v)
            else:
                res[i] = v
        # 然后对char进行排序
        char.sort(key=lambda c: c.lower())
        # 重构,在res中的false项中放入char
        for i, v in enumerate(res):
            if not v:
                res[i] = char[0]
                char.pop(0)
        print(''.join(res))
    except:
        break
