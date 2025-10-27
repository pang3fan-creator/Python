def main(data_path):
    # 读取数据
    with open('./Apriori_data.txt', 'r') as f:
        data_file = [frozenset(item.strip().split(',')) for item in f]
    list_all = [{frozenset([i]): 'None' for item in data_file for i in item}]

    k = 0
    while len(list_all[k]) >= 2:
        dict_k = list_all[k]

        # 数据处理1
        dict_temp1 = {}
        for i in dict_k.keys():
            for j in dict_k.keys():
                i_j = frozenset(i | j)
                if len(i_j) == (k + 1) and i_j not in dict_temp1.keys():
                    dict_temp1.setdefault(i_j, 0)
                    for item in data_file:
                        dict_temp1[i_j] += (1 if i_j <= item else 0)
        # 数据处理2
        dict_temp2 = {}
        for i in dict_temp1:
            if dict_temp1[i] >= 2:
                dict_temp2[i] = dict_temp1[i]

        list_all.append(dict_temp2)
        k += 1


if __name__ == '__main__':
    main('./Apriori_data.txt')
    # 读取数据
    with open('./Apriori_data.txt', 'r') as f:
        data_file = [frozenset(item.strip().split(',')) for item in f]
    list_all = [{frozenset([i]): 'None' for item in data_file for i in item}]

    k = 0
    while len(list_all[k]) >= 2:
        dict_k = list_all[k]

        # 数据处理1
        dict_temp1 = {}
        for i in dict_k.keys():
            for j in dict_k.keys():
                i_j = frozenset(i | j)
                if len(i_j) == (k + 1) and i_j not in dict_temp1.keys():
                    dict_temp1.setdefault(i_j, 0)
                    for item in data_file:
                        dict_temp1[i_j] += (1 if i_j <= item else 0)
        # 数据处理2
        dict_temp2 = {}
        for i in dict_temp1:
            if dict_temp1[i] >= 2:
                dict_temp2[i] = dict_temp1[i]

        list_all.append(dict_temp2)
        k += 1

    for i in list_all:
        print(i)
        print()
