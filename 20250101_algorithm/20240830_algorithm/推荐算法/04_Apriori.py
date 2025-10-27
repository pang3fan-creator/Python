'''
Apriori算法，寻找频繁项集
'''


def load_data(data_file):
    ret = []
    with open(data_file, 'r') as f:
        for line in f.readlines():
            ret.append(line.strip().split(','))
    return ret


def creat_C1(data_set):
    C1 = []
    # 遍历每一条购买记录中的每一个商品
    for transaction in data_set:
        for item in transaction:
            if [item] not in C1:
                C1.append([item])

    C1.sort()

    return list(map(frozenset, C1))


def san_D(D, Ck, min_support):
    ss_cnt = {}  # 记录每一项出现的频率
    # 遍历每一条购买记录
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in ss_cnt:
                    ss_cnt[can] = 1
                else:
                    ss_cnt[can] += 1
    # 购买记录的总数
    num_items = float(len(D))
    retList = []  # 收集当前的频繁项集
    support_data = {}  # 收集每一项的支持度

    # 遍历每一项的频率，计算相对支持度
    for key in ss_cnt:
        support = ss_cnt[key] / num_items  # 出现次数 / 记录总数
        # 过滤最小支持度
        if support >= min_support:
            retList.insert(0, key)
        support_data[key] = support

    return retList, support_data


def apriori_gen(Lk_sub1, k):
    retList = []
    for i in range(len(Lk_sub1) - 1):
        for j in range(i + 1, len(Lk_sub1)):
            if len(Lk_sub1[i] & Lk_sub1[j]) == (k - 2):
                retList.append(Lk_sub1[i] | Lk_sub1[j])

    retList = list(set(retList))

    return retList


def apriori(data_file, min_support=0.5):
    # 加载数据
    data_set = load_data(data_file)
    D = list(map(frozenset, data_set))
    # 生成1项集的候选集
    C1 = creat_C1(data_set)
    # 计算候选集中每一项的支持度，过滤最小支持度，得到频繁项集
    L1, sup_data = san_D(D, C1, min_support)

    L = [L1]  # 保存每一个项的频繁项集
    k = 2  # 要生成下一个候选集的项的个数

    while len(L[k - 2]) >= 2:
        # 根据当前项的频繁项集，来生成下一个项的候选集
        Ck = apriori_gen(L[k - 2], k)
        # 计算每一项的支持度，过滤最小支持度，得到频繁项集
        Lk, sup_k = san_D(D, Ck, min_support)
        L.append(Lk)
        sup_data.update(sup_k)
        k += 1

    return L, sup_data


if __name__ == '__main__':
    L, sup_data = apriori('./Apriori_data.txt')

    # for data in L:
    #     print(data)
    #
    # for i, j in sup_data.items():
    #     print('项集:{},支持度:{}'.format(i, j))
