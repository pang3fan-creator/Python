def rol(str_1, K):
    for __ in range(K):
        str_foront = str_1[0]
        str_back = str_1[1:]
        str_1 = str_back + str_foront
    return str_1


if __name__ == '__main__':
    str_1 = input("请输入字符串：")
    K = input('请输入要循环左移的个数：')
    try:
        K = int(K)
    except ValueError:
        print('输入有误，请重新输入')
        exit()

    result = rol(str_1, K)
    print(result)
