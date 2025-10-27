import math


def get_result():
    row_half, count = math.ceil(row / 2), 1
    for i in range(row_half):
        for j in range(i, column - i):
            list_num[i][j], count = count, count + 1
            if count > num_amount: return
        for k in range(i + 1, row - i):
            list_num[k][column - i - 1], count = count, count + 1
            if count > num_amount: return
        for l in range(column - i - 2, i - 1, -1):
            list_num[row - i - 1][l], count = count, count + 1
            if count > num_amount: return
        for m in range(row - i - 2, i, -1):
            list_num[m][i], count = count, count + 1
            if count > num_amount: return


if __name__ == '__main__':
    num_amount, row = map(int, input().strip().split(' '))
    column = math.ceil(num_amount / row)

    list_num = [['*' for j in range(column)] for i in range(row)]
    get_result()

    for item in list_num: print(' '.join(map(str, item)))
