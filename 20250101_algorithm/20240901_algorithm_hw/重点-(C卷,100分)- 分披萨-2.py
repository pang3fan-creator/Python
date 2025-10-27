# 越界索引环形变化
def check(idx):
    if idx < 0:
        idx = n - 1
    elif idx >= n:
        idx = 0

    return idx


def recursive(l, r):
    # 进入递归前，"吃货"已经拿了披萨，因此进入递归后，轮到"馋嘴"拿
    # 而"馋嘴"拿披萨的策略固定是：缺口左右两边中较大的那块
    if pizza[l] > pizza[r]:  # 注意披萨大小各部相同，因此要么左边大，要么右边大，不存在相等的情况
        # 拿走第 l 块，因此缺口左边的位置变为 l - 1
        l = check(l - 1)
    else:
        # 拿走第 r 块，因此缺口右边的位置变为 r + 1
        r = check(r + 1)

    if cache[l][r] > 0:
        return cache[l][r]

    if l == r:
        # 当 l == r 是，说明只剩一块披萨了，由于奇数个披萨，且"吃货"第一个拿，因此最后一个也是"吃货"拿
        cache[l][r] = pizza[l]
    else:
        # 如果还剩多块披萨，那么"吃货"有两种选择：
        # 1、拿缺口左边的披萨
        # 2、拿缺口右边的披萨
        # 因此这里直接开两个递归分支，最终结果取较大值
        cache[l][r] = max(recursive(check(l - 1), r) + pizza[l], recursive(l, check(r + 1)) + pizza[r])

    return cache[l][r]


if __name__ == '__main__':
    n = int(input())  # 披萨数量（奇数个）

    pizza = [int(input()) for _ in range(n)]  # n个披萨的大小（各不相同）

    cache = [[0] * n for _ in range(n)]  # 缓存表

    # ans记录"吃货"能获得的最大披萨大小
    ans = 0

    for i in range(n): ans = max(ans, recursive(check(i - 1), check(i + 1)) + pizza[i])

    print(ans)
