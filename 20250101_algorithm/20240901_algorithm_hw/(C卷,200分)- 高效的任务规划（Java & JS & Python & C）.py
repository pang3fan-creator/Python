def main(list_n):
    time_use, time_left = 0, 0
    for item in list_n:
        time_use, time_left = time_use + item[0], max(time_left - item[0], item[1])
    return time_use + time_left


if __name__ == '__main__':
    res = []
    for i in range(int(input())):
        list_n = [list(map(int, input().split(' '))) for _ in range(int(input()))]
        list_n = sorted(list_n, key=lambda x: x[1], reverse=True)
        res.append(main(list_n))
    [print(i) for i in res]
