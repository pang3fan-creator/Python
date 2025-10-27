def get_result():
    length, count = 1, 0
    while length <= N:
        length_left = len(list_n) - length + 1
        for i in range(length_left):
            if sum(list_n[i:i + length]) >= x:
                count += length_left - i
                break
        length += 1
    return count


if __name__ == '__main__':
    N, x = map(int, input().split(' '))
    list_n = sorted(map(int, input().strip().split(' ')))
    print(get_result())
