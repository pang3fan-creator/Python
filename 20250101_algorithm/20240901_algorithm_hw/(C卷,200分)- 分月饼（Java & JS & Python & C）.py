"""
题目描述
中秋节，公司分月饼，m 个员工，买了 n 个月饼，m ≤ n，每个员工至少分 1 个月饼，但可以分多个，

单人分到最多月饼的个数是 Max1 ，单人分到第二多月饼个数是 Max2 ，Max1 - Max2 ≤ 3 ，
单人分到第 n - 1 多月饼个数是 Max(n-1)，单人分到第n多月饼个数是 Max(n) ，Max(n-1) – Max(n) ≤ 3,
问有多少种分月饼的方法？

输入描述
每一行输入m n，表示m个员工，n个月饼，m ≤ n

输出描述
输出有多少种月饼分法
"""


def recursive(level, low, high, remain):
    """
    level: 第几个员工
    low: 当前员工至少分得几个月饼
    high: 当前员工至多分得几个月饼
    remain: 分月饼给当前员工前，月饼的剩余数量
    """
    global ans

    # 分到最后一个员工时，我们应该将剩余月饼都给他
    if level == m - 1:
        # 因此最后一个员工的月饼数量就是remain，而倒数第二个员工的月饼数量是low（本轮递归的min参数，即上一轮员工分得的月饼数量）
        if remain - low <= 3:
            ans += 1  # 如果二者差距不超过maxDiff，则分月饼方案可行
        return

    # i 是当前员工可以分得的月饼数量
    for i in range(low, high + 1):
        remain -= i
        # 下一个员工至少分得 i 个月饼（当前员工分得的月饼数量），至多分得 i + maxDiff
        # 同时下一个员工分得的月饼数量不能超过：均分月饼数量（即剩余月饼总数 / 剩余员工总数），否则破坏去重策略（为了保证分月饼的方案不重复，我们这里保证后面的员工分得月饼数不小于前面员工）
        recursive(level + 1, i, min(i + 3, remain // (m - level - 1)), remain)
        remain += i


def main():
    if m == 1 or n == m: return 1  # 如果只有一个员工分月饼，那么就只有一种方案

    # 如果有多个员工分月饼，为了保证分月饼的方案不重复，我们这里保证 员工i的月饼数量 <= 员工i+1的月饼数量
    # 因此对于第0个员工，至少分得1个月饼，至多分得n/m个月饼（均分数量）
    recursive(0, 1, n // m, n)
    return ans


if __name__ == '__main__':
    (m, n), ans = map(int, input().split()), 0

    print(main())
