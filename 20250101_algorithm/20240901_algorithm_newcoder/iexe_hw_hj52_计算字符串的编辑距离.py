"""
编辑距离：Levenshtein 距离，用来衡量两个字符串之间转换所需的最少编辑操作次数。编辑操作包括：插入一个字符、删除一个字符、或替换一个字符。
计算最小编辑距离的基本算法可以使用动态规划。还有一些变体可以优化时间或空间复杂度，或者增加其他特性（如加权编辑距离）。Levenshtein 距离在大多数情况下是用于测量两个字符串之间的相似度，是字符串比对和文本处理领域常用的方法之一。
注意：
插入操作和删除操作是等价的，str1删除n次可以得到str2，那么str2也可以插入n次得到str1，具体如何操作就要看这两个操作的代价哪个小就选哪个
"""


def editing_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    del_cost = 1  # 删除成本
    insert_cost = 1  # 插入成本
    replace_cost = 1  # 替换成本
    min_const = min(insert_cost, del_cost)
    """
    这里需要得到一个插入和删除中的更小的一个成本，
    因为如果当第二个字符串去除最后一位就等于第一个字符串时
    如str1='abc'，str2='abcd'
    他们的编辑可以是删除str2的最后一位，或者在str1的最后面插入
    编辑距离应该是这两者中小的一个
    但是有一个点是插入会加长字符串，如果有要求必须最后的两个字符编辑完的状态是长度最短
    那么必须选择删除操作
    """
    # dp[i][j]代表str1前i个字符与str2前j个字符的最小编辑距离
    # 初始化dp，长度为零的字符串和另一个字符串的编辑距离就是第二个字符长度长度乘以小成本(删除和插入中小的一个成本)
    for i in range(m + 1):
        dp[i][0] = i * min_const
    for j in range(n + 1):
        dp[0][j] = j * min_const

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                """给出的三个成本删除，插入，替换成本"""
                dp[i][j] = min(
                    dp[i - 1][j] + min_const,
                    dp[i][j - 1] + min_const,
                    dp[i - 1][j - 1] + replace_cost
                )
    return dp[m][n]


import sys

lines = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    lines.append(line)
str1 = lines[0]
str2 = lines[1]

print(editing_distance(str1, str2))
