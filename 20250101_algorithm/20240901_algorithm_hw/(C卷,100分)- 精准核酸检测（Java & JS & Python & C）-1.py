# 并查集实现
class UnionFindSet:
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        return x

    def union(self, x, y):
        x_fa = self.find(x)
        y_fa = self.find(y)

        if x_fa != y_fa:
            self.fa[y_fa] = x_fa


# 算法入口
def getResult():
    ufs = UnionFindSet(n)

    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] == 1:
                # 有过接触的人进行合并
                ufs.union(i, j)

    # 统计每个接触群体（连通分量）中的人数
    cnts = [0] * n
    for i in range(n):
        fa = ufs.find(i)
        cnts[fa] += 1

    # 记录已统计过的可能感染群体
    confirmed_fa = set()

    # 将有感染者的接触群体的人数统计出来
    ans = 0
    for i in confirmed:
        fa = ufs.find(i)

        # 已统计过的可能感染群体不再统计
        if fa in confirmed_fa:
            continue
        confirmed_fa.add(fa)

        ans += cnts[fa]

    # 最终需要做核酸的人数，不包括已感染的人
    return ans - len(confirmed)


if __name__ == '__main__':
    # 输入获取
    n = int(input())
    confirmed = list(map(int, input().split(",")))
    matrix = [list(map(int, input().split(","))) for _ in range(n)]

    # 算法调用
    print(getResult())
