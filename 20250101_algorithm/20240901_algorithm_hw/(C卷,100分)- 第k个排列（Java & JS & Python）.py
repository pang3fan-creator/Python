def make_recursion(n):
    if n == 0: return 1
    return n * make_recursion(n - 1)


if __name__ == '__main__':
    n, k = int(input()) - 1, int(input()) - 1
    list_n = [str(i) for i in range(1, n + 2, 1)]

    str_n = ''
    while list_n:
        r = make_recursion(n)
        t, k, n = k // r, k % r, n - 1
        str_n = str_n + list_n.pop(t)
    print(str_n)
    # while k != 0 and n != 0:
    #     r = make_recursion(n)
    #     t, k, n = k // r, k % r, n - 1
    #     str_n = str_n + list_n.pop(t)
    # print(str_n + ''.join(list_n))
