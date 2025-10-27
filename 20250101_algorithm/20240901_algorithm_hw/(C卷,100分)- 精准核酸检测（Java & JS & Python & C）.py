# 并查集实现
class UnionFindSet:
    def __init__(self, n):
        self.fa = [0 for __ in range(n)]

    def find(self, x):
        return self.fa[x]

    def union(self, x, y):
        x_fa = self.find(x)
        y_fa = self.find(y)

        if x_fa != y_fa: self.fa[x] = self.fa[y] = 1


if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            if N not in range(0, 100): break
            ufs = UnionFindSet(N)

            list_index = list(map(int, input().split(',')))
            for i in list_index: ufs.fa[i] = 1

            msgs = [list(map(int, input().split(','))) for _ in range(N)]
            for i in range(N):
                for j in range(0, i): ufs.union(i, j) if msgs[i][j] == 1 else None

            print(len(ufs.fa) - len(list_index))
        except:
            break
