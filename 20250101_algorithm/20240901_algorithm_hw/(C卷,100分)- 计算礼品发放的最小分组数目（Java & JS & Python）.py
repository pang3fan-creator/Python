if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            list_n = sorted(list(map(int, input().strip().split(' '))))
            print(list_n)
            count = 0
            while list_n:
                a = list_n.pop(-1)
                if a >= N: count += 1; continue
                for i in range(len(list_n) - 1, -1, -1):
                    if a + list_n[i] <= N:
                        list_n.pop(i)
                        break
                count += 1
            print(count)
        except:
            break
