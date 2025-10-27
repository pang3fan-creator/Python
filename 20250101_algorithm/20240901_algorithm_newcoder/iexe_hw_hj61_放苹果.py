"""
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。
"""


def f(m, n):
    if m < 0: return 0
    if n == 1: return 1
    return f(m - n, n) + f(m, n - 1)


while True:
    try:
        m, n = map(int, input().split(' '))  # 苹果的数量# 盘子的数量
        print(f(m, n))
    except:
        break
