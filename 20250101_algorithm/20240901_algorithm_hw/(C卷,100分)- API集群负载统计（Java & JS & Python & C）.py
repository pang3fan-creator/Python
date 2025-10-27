while True:
    try:
        dict_str = {}
        for __ in range(int(input())):
            list_str = input().strip()[1::].split('/')
            for i, j in enumerate(list_str):
                dict_str.setdefault(i + 1, {}), dict_str[i + 1].setdefault(j, 0)
                dict_str[i + 1][j] += 1
        N, str_query = input().strip().split(' ')
        N = int(N)
        num_N = dict_str.get(N, 0)
        print(0) if num_N == 0 else print(num_N.get(str_query, 0))
    except:
        break
