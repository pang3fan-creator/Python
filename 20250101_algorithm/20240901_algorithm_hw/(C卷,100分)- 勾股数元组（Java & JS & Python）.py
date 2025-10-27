import math
import time


def judge_prime(i, j):
    while True:
        if j - i == 1: return True
        if j % i == 0: return False
        i, j = sorted((i, j % i))


def get_res(N, M):
    if N not in range(1, 10000): return
    if M not in range(N + 1, 10001): return
    list_1 = [i ** 2 for i in range(N, M + 1)]
    set_1 = set(list_1)
    list_2 = []
    for i in range(len(list_1)):
        for j in range(i + 1, len(list_1)):
            temp = list_1[i] + list_1[j]
            if temp in set_1 and judge_prime(list_1[i], list_1[j]):
                list_2.append((int(math.sqrt(list_1[i])), int(math.sqrt(list_1[j])), int(math.sqrt(temp))))
    if not list_2:
        print('NA')
    else:
        for i in list_2: print(f'{i[0]} {i[1]} {i[2]}')


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    a = time.time()
    get_res(N, M)
    print(time.time() - a)
