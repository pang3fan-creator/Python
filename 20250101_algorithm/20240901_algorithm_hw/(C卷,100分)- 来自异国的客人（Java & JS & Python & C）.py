if __name__ == '__main__':
    while True:
        try:
            k, n, m = map(int, input().split(' '))
            count = 0
            while k:
                s, k = k % m, k // m
                if s == n: count += 1
            print(count)


        except:
            pass
