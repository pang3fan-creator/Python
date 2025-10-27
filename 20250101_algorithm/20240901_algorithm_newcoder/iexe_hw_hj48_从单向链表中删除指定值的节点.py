while True:
    try:
        string = list(map(int, input().split()))
        link = []  # 链表
        link.append(string[1])  # 表头
        for i in range(1, string[0]):
            link.insert(link.index(string[2 * i + 1]) + 1, string[2 * i])

        link.remove(string[-1])
        print(' '.join(map(str, link)))
    except:
        break
