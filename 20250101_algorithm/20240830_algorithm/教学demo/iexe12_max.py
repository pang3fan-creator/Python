import random


def maxInWindows(list_n, W, width):
    list_temp = [max(list_n[i:i + W]) for i in range(width)]
    return list_temp


if __name__ == '__main__':
    N = int(input("请输入要生成的随机数个数："))
    list_n = [random.randint(1, 501) for i in range(N)]
    print(list_n)
    W = 3
    width = N - W + 1
    print(maxInWindows(list_n, W, width))
