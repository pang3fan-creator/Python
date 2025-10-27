"""
冒泡排序
"""

times = 0


def bubble_sort(li):
    global times
    # 代码第2步: 如果不知道循环几次，则举几个示例来判断
    for j in range(0, len(li) - 1):
        # 代码第1步: 此代码为一波比对，此段代码一定一直循环，一直比对多次至排序完成
        for i in range(0, len(li) - j - 1):
            times += 1
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]

    return li


import random

L = []
N = 10000
for i in range(N):
    L.append(random.randint(1, N))
print(L)
bubble_sort(L)
print(L)
print("循环次数：", times)
