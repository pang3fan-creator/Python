# 二叉树递归
def binary_tree(index):
    if index - 1 == 0: return list_tree[0]
    res = list_tree[index - 1] + binary_tree(index // 2)
    return res


if __name__ == '__main__':
    list_tree = list(map(int, input().strip().split(' ')))
    max_time = 0
    for i in range(len(list_tree), 0, -1):
        if list_tree[i - 1] == -1: continue
        max_time = max(max_time, binary_tree(i))
    print(max_time)
