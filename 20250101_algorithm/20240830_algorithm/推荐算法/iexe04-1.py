def create_comb(data_file, dict_k, k, length):
    set_i_j = set(frozenset(i | j) for i in dict_k.keys() for j in dict_k.keys()
                  if len(frozenset(i | j)) == (k + 1))
    return {i_j: sum(1 for item in data_file if i_j <= item) / length for i_j in set_i_j}


def create_rate(dict_temp1, rate=0.2):
    return {i: j for i, j in dict_temp1.items() if j >= rate}


def main(data_path):
    with open(data_path, 'r') as f:
        data_file = [frozenset(item.strip().split(',')) for item in f]
    list_all = [{frozenset([i]): 'None' for item in data_file for i in item}]

    k = 0
    while len(list_all[-1]) >= 2:
        dict_temp1 = create_comb(data_file, list_all[-1], k, len(data_file))
        dict_temp2 = create_rate(dict_temp1, rate=0.2, )
        list_all.append(dict_temp2)
        k += 1
    return list_all


if __name__ == '__main__':
    list_total = main('./Apriori_data.txt')
    [(print(i), print()) for i in list_total]
