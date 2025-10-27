if __name__ == '__main__':
    N = sorted(map(int, input().strip().split(',')))
    weight_max = int(input())
    weight_count, count = 0, 0
    for num in N:
        weight_count += num
        if weight_count > weight_max: break
        count += 1
    print(count)
