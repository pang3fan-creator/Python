def get_result():
    dict_n = {}
    for i in range(n - 1):
        num_1, num_2 = map(int, input().split(' '))
        dict_n.setdefault(num_1, list_n[num_1])
        dict_n[num_1] += list_n[num_2]
    return sorted(dict_n.values(), reverse=True)[0]


if __name__ == '__main__':
    n = int(input())
    list_n = list(map(int, input().split(' ')))
    list_n.insert(0, 0)
    print(get_result())
