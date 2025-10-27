from functools import cache


def check(idx):
    if idx < 0:
        idx = n - 1
    elif idx >= n:
        idx = 0

    return idx


@cache
def recursive(l, r):
    if pizza[l] > pizza[r]:
        l = check(l - 1)
    else:
        r = check(r + 1)

    if l == r:
        return pizza[l]
    else:
        return max(recursive(check(l - 1), r) + pizza[l], recursive(l, check(r + 1)) + pizza[r])


if __name__ == '__main__':

    n = int(input())  # 披萨数量（奇数个）

    pizza = [int(input()) for _ in range(n)]  # n个披萨的大小（各不相同）

    ans = 0  # ans记录"吃货"能获得的最大披萨大小

    for i in range(n):  ans = max(ans, recursive(check(i - 1), check(i + 1)) + pizza[i])

    print(ans)
