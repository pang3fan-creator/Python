'''
首先应该明确示例的定义，示例对于理解题目来说非常关键
输入第一行，1000 是总预算（total_budget） 5 指总的物品数量（包含主件附件）
第二行之后的就是每个物品的描述数据了
第一列800 400 300 400 500 这些表示物品价格，第二列的数字是物品的重要度
第三列很关键，，非0 数字都表示这个物品是附件，0 表示这个物品是主件。
非0的同时这个数字是和主件有绑定关系的，比如是1，表示这个是主件1 的附件，那么主件1 是谁就很关键，
找错主件结果就完全不对了，所以这里要考虑我们在存储主件的时候，同时要保留的是主件的索引，从题目中来看，主件从1 开始
所以遇到第1行是0 的数据，就得更新主件索引为1（i + 1），同时将附件数据绑定上去，这样算是成功了一半了。

多重背包很关键的一点考虑在物品不能重复购买，这就说明你在预算计算的时候，需要考虑是倒序遍历
必须的，不然重复计算了，这点可能比较难理解，可以带入一下就能想的比较清晰，还有一点就是遍历时的stop 点
v - 1 , 当j >= v 的时候进行遍历即可
思考，先从主件开始，主件+附件1 主件+附件2 主件+附件1+附件2，依次更新dp[j]

#购物单 这是一个多重背包问题,购买主件后，可以不购买附件，也可以购买1件或者2件附件，不能重复购买，求最大的满意度
#首先定义这个输入输出

1000 总预算 5物品数量
800 2 满意度 0 主件0
400 5 1 主件0 的附件1
300 5 1 主件0 的附件2
400 3 0 主件1
500 2 0 主件2
'''
import sys

total_budget, num_items = map(int, sys.stdin.readline().rstrip().split())

# 存储主件
main_items = []
attachments = {}
i = 0
while i < num_items:
    v, p, q = map(int, sys.stdin.readline().rstrip().split())
    if q == 0:  # 存储主件
        main_items.append((v, p, i + 1))
    else:  # 附件
        if q not in attachments:
            attachments[q] = []
        attachments[q].append((v, p))
    i += 1

dp = [0] * (total_budget + 1)
# 选择主件
for v, p, idx in main_items:
    # 从后往前遍历，避免重复选择
    for j in range(total_budget, v - 1, -1):
        dp[j] = max(dp[j], dp[j - v] + v * p)
        # 计算附件
        if idx in attachments:
            for av, ap in attachments[idx]:
                if j >= v + av:
                    dp[j] = max(dp[j], dp[j - v - av] + v * p + av * ap)
            if len(attachments[idx]) == 2:
                av1, ap1 = attachments[idx][0]
                av2, ap2 = attachments[idx][1]
                if j >= av1 + av2 + v:
                    dp[j] = max(dp[j], dp[j - v - av1 - av2] + v * p + av1 * ap1 + av2 * ap2)

print(dp[total_budget])
