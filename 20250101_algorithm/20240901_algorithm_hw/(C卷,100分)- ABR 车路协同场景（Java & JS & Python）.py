while True:
    try:
        A, B, R = input().strip().split('},')
        A = sorted(list(map(int, A.replace('A={', '').split(','))))
        B = sorted(list(map(int, B.replace('B={', '').split(','))))
        R = int(R.replace('R=', ''))
        list_num = []
        for i in A:
            list_temp = []
            for j in B:
                if i <= j and i + j <= R:
                    list_temp.append((i, j,))
                elif i <= j and i + j > R and not list_temp:
                    list_temp.append((i, j,))
                    break
            list_num.extend(list_temp)
        print(list_num)


    except:
        break
