if __name__ == '__main__':
    num = int(input())
    list_num = sorted(map(int, input().strip().split(' ')), reverse=False)
    N = int(input())
    count = 0
    l, r = 0, len(list_num) - 1
    while l <= r:
        if list_num[r] >= N:
            count += 1
            r -= 1
            continue
        if list_num[l] + list_num[r] >= N:
            count += 1
            r -= 1
            l += 1
            continue
        else:
            l += 1
    print(count)
