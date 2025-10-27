class Project:
    def __init__(self, name, hot):
        self.name = name
        self.hot = hot


if __name__ == '__main__':

    # 输入获取
    n = int(input())

    weights = list(map(int, input().split()))

    projects = []
    for _ in range(n):
        tmp = input().split()

        name = tmp.pop(0)

        statistics = list(map(int, tmp))

        hot = 0
        for i in range(5): hot += statistics[i] * weights[i]

        projects.append(Project(name, hot))

    projects.sort(key=lambda x: (-x.hot, x.name.lower()))

    for p in projects: print(p.name)
