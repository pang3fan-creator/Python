if __name__ == '__main__':
    while True:
        try:
            N, list_n, M = int(input()), list(map(int, input().strip().split(' '))), int(input())
            sum_max = 0
            for i in range(N - M + 1): sum_max = max(sum_max, sum(list_n[i:i + M]))
            print(sum_max)
        except:
            break
