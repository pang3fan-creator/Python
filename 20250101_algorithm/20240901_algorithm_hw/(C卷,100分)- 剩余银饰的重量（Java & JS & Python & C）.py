def binary_search(res):
    l, r = 0, len(list_n) - 1
    while l <= r:
        mid = (l + r) // 2
        if res == list_n[mid]:
            list_n.insert(mid + 1, res)
            return
        elif res > list_n[mid]:
            l = mid + 1
        else:
            r = mid - 1
    list_n.insert(mid + 1, res)


def get_result():
    while list_n:
        if len(list_n) == 1: return list_n[0]
        if len(list_n) == 2: return max(list_n[0], list_n[1])
        z, y, x = list_n.pop(-1), list_n.pop(-1), list_n.pop(-1)
        res = abs((z - y) - (y - x))
        if len(list_n) == 0: return res
        if res != 0: binary_search(res)


if __name__ == '__main__':
    N = int(input())
    list_n = sorted(map(int, input().split(' ')))
    print(get_result())
