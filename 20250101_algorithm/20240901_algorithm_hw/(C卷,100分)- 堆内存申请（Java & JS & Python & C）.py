def use_memory(param):
    for i in range(param[1]): l_memory_f.append([param[0] + i, False])


def input_memory():
    temp = int(input())
    while True:
        try:
            use_memory(list(map(int, input().strip().split(' '))))
        except:
            break
    return temp


if __name__ == '__main__':
    l_memory_f = [[-1, False], [100, False]]
    n_memory = input_memory()

    l_memory_f = sorted(l_memory_f, key=lambda x: x[0])
    for i, (j, flag) in enumerate(l_memory_f):
        if i == 0: continue
        start = l_memory_f[i - 1][0] + 1
        if j - start >= n_memory: print(start), exit()
    print(-1)
