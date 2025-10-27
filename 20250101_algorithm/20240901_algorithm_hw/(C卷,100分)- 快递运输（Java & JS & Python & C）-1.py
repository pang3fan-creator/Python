# 输入获取
weights = list(map(int, input().split(",")))
limit = int(input())


# 算法入口
def getResult():
    weights.sort()

    total = 0
    count = 0
    for w in weights:
        total += w
        if total > limit:
            break
        count += 1

    return count


# 调用算法
print(getResult())
