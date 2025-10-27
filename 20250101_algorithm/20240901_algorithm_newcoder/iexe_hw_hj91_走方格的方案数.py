"""
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角
总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
"""


def f(n, m):
    # 退出条件
    if n == 0 and m == 0: return 1
    if n < 0 or m < 0: return 0
    # 可分解的问题,向出口靠近
    a = f(n - 1, m) + f(n, m - 1)
    return a


while True:
    try:
        n, m = map(int, input().split())
        print(f(n, m))
    except:
        break
