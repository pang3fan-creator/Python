if __name__ == '__main__':
    while True:
        try:
            m, n = map(int, input().strip().split(' '))

            dict_xy = {}
            for y in range(m):
                list_mn = list(map(int, input().strip().split(' ')))
                for x in range(n):
                    res = list_mn[x]
                    if res != 0: dict_xy[res] = dict_xy.get(res, []) + [[y, x]]

            area = 0
            for k, v in dict_xy.items():
                y_max, y_min = max([i[0] for i in v]), min([i[0] for i in v])
                x_max, x_min = max([i[1] for i in v]), min([i[1] for i in v])
                area = max(area, (y_max - y_min + 1) * (x_max - x_min + 1))
            print(area)
        except:
            break
