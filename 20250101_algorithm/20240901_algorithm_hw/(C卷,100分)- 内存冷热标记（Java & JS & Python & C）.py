if __name__ == '__main__':
    n = int(input())
    list_seq = list(map(int, input().strip().split(' ')))
    N = int(input())
    dict_seq = {}
    for i in range(n):
        dict_seq[list_seq[i]] = dict_seq.get(list_seq[i], 0) + 1
    items_seq = filter(lambda x: x[1] >= N, dict_seq.items())
    items_seq = sorted(items_seq, key=lambda x: x[1], reverse=True)
    if len(items_seq) == 0:
        print(0)
    else:
        print(len(items_seq))
        for num, _ in items_seq:
            print(num)
