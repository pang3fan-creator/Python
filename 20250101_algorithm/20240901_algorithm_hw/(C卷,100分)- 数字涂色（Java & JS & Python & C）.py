if __name__ == '__main__':
    N, list_n = int(input()), sorted(map(int, input().strip().split(' ')))
    list_color = [list_n.pop(0)]

    for i in range(N - 1):
        for j, num in enumerate(list_color):
            if list_n[i] % num == 0: break
            if j == len(list_color) - 1: list_color.append(list_n[i])
    print(len(list_color))
