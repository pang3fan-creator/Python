if __name__ == '__main__':
    N = int(input())
    min_n, max_m = map(int, input().split(' '))
    for __ in range(1, N):
        item = list(map(int, input().split(' ')))
        if min_n <= item[0] <= max_m:
            min_n, max_m = min(item[0], min_n), max(item[1], max_m)
        else:
            print(f'{min_n} {max_m}')
            min_n, max_m = item[0], item[1]
    print(f'{min_n} {max_m}')
