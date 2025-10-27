while True:
    try:
        list_n = list(map(int, input().split(' ')))
        dict_n = {}
        for i in list_n: dict_n[i] = dict_n.get(i, 0) + 1

        max_value = max(dict_n.values())
        list_sorted = sorted([int(k) for k, v in dict_n.items() if v == max_value])

        length = len(list_sorted)
        if length % 2 == 1:
            print(list_sorted[(length - 1) // 2])
        else:
            a = list_sorted[length // 2 - 1]
            b = list_sorted[length // 2]
            print((a + b) / 2)
    except:
        break
