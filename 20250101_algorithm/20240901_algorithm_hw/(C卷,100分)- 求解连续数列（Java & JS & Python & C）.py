def get_result():
    res = sum_n / n - n / 2 + 0.5
    if res <= 0: return [-1]
    if int(res) != res: return [-1]
    list_res = []
    for i in range(n):
        list_res.append(int(res))
        res += 1
    return list_res


if __name__ == '__main__':
    sum_n, n = map(int, input().strip().split(' '))
    print(' '.join(map(str, get_result())))
