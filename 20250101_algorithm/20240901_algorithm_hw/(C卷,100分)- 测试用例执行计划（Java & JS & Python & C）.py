# 输入获取
n, m = map(int, input().split())

features = [0] * (n + 1)
for i in range(1, n + 1):
    features[i] = int(input())

cases = []
for i in range(1, m + 1):
    priority = sum(map(lambda x: features[int(x)], input().split()))
    cases.append([priority, i])

cases.sort(key=lambda x: (-x[0], x[1]))

for _, idx in cases:
    print(idx)
