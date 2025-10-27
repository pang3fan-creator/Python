def find_num(N, M):
    if N not in range(3, 8): return -1
    count = -1
    for i in range(10 ** (N - 1), 10 ** N):
        sum_sum = sum(map(lambda x: int(x) ** 3, list(str(i))))
        if sum_sum == i: count += 1
        if count == M: return i
    return -1


if __name__ == '__main__':
    while True:
        try:
            N, M = int(input()), int(input())
            print(find_num(N, M))
        except:
            break
