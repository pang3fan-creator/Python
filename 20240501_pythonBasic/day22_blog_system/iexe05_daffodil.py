def judeg_daffodil(param):
    list_temp = []
    for i in range(0, param, 1):
        res = sum(map(lambda x: int(x) ** 3, str(i)))
        if res == i: list_temp.append(i)
    return list_temp


if __name__ == '__main__':
    list_n = judeg_daffodil(int(input()))
    print(list_n)
