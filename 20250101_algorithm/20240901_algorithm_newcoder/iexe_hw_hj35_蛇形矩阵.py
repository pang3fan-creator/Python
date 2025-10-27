"""
输入正整数N（N不大于100）
输出一个N行的蛇形矩阵。
"""

while True:
    try:
        n = int(input())
        a = [[0 for i in range(n)] for j in range(n)]
        count = 1
        for total in range(0, n, 1):
            for j in range(total, -1, -1):
                a[j][total - j] = count
                count += 1
        for i in a:
            for j in i:
                if j != 0:
                    print(int(j), end=' ')
                else:
                    break
            print()
    except:
        break
