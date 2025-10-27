# 输入获取
heights = list(map(int, input().split(",")))


# 算法入口（本题实际考试为核心代码模式，因此考试时只需要写出此函数实现即可）
def getResult(h):
    count = 0

    for i in range(len(h)):
        leftH = h[i - 1] if i - 1 >= 0 else 0
        rightH = h[i + 1] if i + 1 < len(h) else 0

        if h[i] > leftH and h[i] > rightH:
            count += 1

    return count


# 算法调用
print(getResult(heights))
