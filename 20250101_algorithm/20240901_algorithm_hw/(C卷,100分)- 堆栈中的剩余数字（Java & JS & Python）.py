def dfs(item):
    num_sum = 0
    for i in range(len(list_new) - 1, -1, -1):
        num_sum += list_new[i]
        if num_sum == item:
            del list_new[i:len(list_new):1]
            return dfs(2 * item)
    return item


if __name__ == '__main__':
    while True:
        try:
            list_new = []
            list_N = list(map(int, input().strip().split(' ')))
            while list_N: list_new.append(dfs(list_N.pop(0)))
            print(' '.join(map(str, list_new[::-1])))
        except:
            break
