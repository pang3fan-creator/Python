import random


def rank(list_n, N):
    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            try:
                if list_n[i] > list_n[j]:
                    list_n[i], list_n[j] = list_n[j], list_n[i]
                elif list_n[i] == list_n[j]:
                    list_n.remove(list_n[i])
                else:
                    continue
            except:
                continue
    return list_n


if __name__ == '__main__':
    N = int(input("请输入要生成的随机数个数："))
    list_n = [random.randint(1, 501) for i in range(N)]
    print(list_n)
    print(rank(list_n, N))
