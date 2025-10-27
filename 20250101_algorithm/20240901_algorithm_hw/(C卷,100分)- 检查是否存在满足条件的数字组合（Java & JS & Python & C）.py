if __name__ == '__main__':
    while True:
        try:
            list_n = map(int, input().split(' '))
            list_n = sorted(list_n)
            while list_n:
                A = list_n.pop(-1)
                for i in range(len(list_n) - 1, 0, -1):
                    for j in range(i - 1, -1, -1):
                        if A == list_n[i] + 2 * list_n[j]:
                            print(f'{A} {list_n[i]} {list_n[j]}')
                            break
        except:
            break
