# 输入获取
s = input()


# 算法入口
def getResult():
    # s中'o'的个数
    zeroCount = 0

    for c in s:
        if c == 'o':
            zeroCount += 1

    if zeroCount % 2 == 0:
        return len(s)
    else:
        return len(s) - 1


# 算法调用
print(getResult())
