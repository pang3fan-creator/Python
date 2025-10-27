while True:
    try:
        r = list(map(str, input().split(';')))[:-1]
        r0 = list(r[0].split())[1:]
        numA = list(map(int, r0[0].split('-')))  # 商品数量
        numB = list(map(int, r0[1].split('-')))
        numB.reverse()
        price = [2, 3, 4, 5, 8, 6]
        miane = [10, 5, 2, 1]
        m = 0  # 投币余额
        print('S001:Initialization is successful')
        for i in range(1, len(r)):
            r2 = list(r[i].split())
            if len(r2) == 2:
                com, mon = r[i].split()
            else:
                com = r2[0][0]
                mon = -1
            if com == 'p':  # 投币
                mon = int(mon)
                if mon != 1 and mon != 2 and mon != 5 and mon != 10:
                    print('E002:Denomination error')
                    continue
                if mon != 1 and mon != 2:
                    if (numB[3] + 2 * numB[2]) < mon:
                        print('E003:Change is not enough, pay fail')
                        continue
                if numA[0] == 0 and numA[1] == 0 and numA[2] == 0 and numA[3] == 0 and numA[4] == 0 and numA[5] == 0:
                    print('E005:All the goods sold out')
                    continue
                m += mon  # 投币余额
                print('S002:Pay success,balance=' + str(m))
                for i in range(4):
                    if mon == miane[i]: numB[i] += 1
            if com == 'b':
                if mon[0] != 'A' or int(mon[1]) not in range(1, 7):
                    print('E006:Goods does not exist')
                elif numA[int(mon[1]) - 1] == 0:
                    print('E007:The goods sold out')
                elif m < price[int(mon[1]) - 1]:
                    print('E008:Lack of balance')
                else:
                    numA[int(mon[1]) - 1] -= 1  # 商品数减少
                    m -= price[int(mon[1]) - 1]  # 投币余额减少
                    print('S003:Buy success,balance=' + str(m))
            if com == 'c':  # 退币
                res = m  # 投币余额
                l = []  # 退币张数
                if m == 0:
                    print('E009:Work failure')
                else:
                    for i in range(4):

                        if int(res / miane[i]) <= numB[i]:  # 够张数
                            l.append(int(res / miane[i]))
                            numB[i] -= l[i]  # 存钱减少
                        else:  # 不够
                            l.append(0)
                        res = res - miane[i] * l[i]

                    m = 0  # 余额清零
                    for i in [3, 2, 1, 0]:  # 输出
                        print(str(miane[i]), 'yuan coin number=' + str(l[i]))
            if com == 'q':
                if int(mon) == -1:
                    print('E010:Parameter error')
                else:
                    type = int(mon)
                    if type == 0:
                        for i in range(6):
                            print('A' + str((i + 1)), str(price[i]), str(numA[i]))
                    if type == 1:
                        for i in [3, 2, 1, 0]:
                            print(str(miane[i]), 'yuan coin number=' + str(numB[i]))
    except:
        break
