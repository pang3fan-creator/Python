# 输入获取
n = int(input())
arr = [input() for _ in range(n)]


# 算法入口
def getResult():
    arr.sort(reverse=True)
    stack = [arr.pop()]

    while len(arr) > 0:
        time = arr.pop()
        top = stack[-1]

        if top == time or top[:19] != time[:19]:
            stack.append(time)

    return len(stack)


# 算法调用
print(getResult())
