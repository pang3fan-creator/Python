if __name__ == '__main__':
    while True:
        try:
            list_str = input().strip().split(' ')
            l_yx = [(int(i), int(j)) for i, j in zip(list_str[0::2], list_str[1::2])]
            for i in range(len(l_yx) - 2, 0, -1):
                y_1, y_2 = l_yx[i][0] - l_yx[i - 1][0], l_yx[i + 1][0] - l_yx[i][0]
                x_1, x_2 = l_yx[i][1] - l_yx[i - 1][1], l_yx[i + 1][1] - l_yx[i][1]

                y_1 = y_1 // abs(y_1) if y_1 != 0 else 0
                y_2 = y_2 // abs(y_2) if y_2 != 0 else 0
                x_1 = x_1 // abs(x_1) if x_1 != 0 else 0
                x_2 = x_2 // abs(x_2) if x_2 != 0 else 0

                if (y_1 == y_2) and (x_1 == x_2): l_yx.pop(i)
            for item in l_yx: print(f'{item[0]} {item[1]}', end=' ')
            print()
        except:
            break
