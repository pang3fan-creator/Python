if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            weight = list(map(int, input().split(' ')))

            dict_info = {}
            for __ in range(N):
                str_info = input().strip().split(' ')
                name_info = str_info.pop(0)
                num_info = list(map(int, str_info))
                for i in range(5):
                    dict_info[name_info] = dict_info.get(name_info, 0) + num_info[i] * weight[i]

            items_info = sorted(dict_info.items(), key=lambda x: (-x[1], x[0]), )
            for item in items_info:
                print(item[0])
        except:
            break
