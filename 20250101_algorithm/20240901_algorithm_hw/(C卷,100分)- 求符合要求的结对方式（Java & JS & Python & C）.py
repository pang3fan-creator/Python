if __name__ == '__main__':
    n, arr, m = int(input()), sorted(map(int, input().split(' '))), int(input())
    count = 0
    for i in range(n - 1):
        if arr[i] > m: break
        if arr[i] == m:  count += 1; continue
        for j in range(i + 1, n):
            if arr[i] + arr[j] > m: break
            if arr[i] + arr[j] < m: continue
            if arr[i] + arr[j] == m: count += 1
    print(count)
