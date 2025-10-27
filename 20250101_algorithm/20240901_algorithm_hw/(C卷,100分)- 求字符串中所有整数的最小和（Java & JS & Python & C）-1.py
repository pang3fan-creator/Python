# 算法入口
def getResult():
    isNegative = False
    negative = []

    ans = 0
    for c in s:
        if '0' <= c <= '9':
            if isNegative:
                negative.append(c)
            else:
                ans += int(c)
        else:
            if isNegative and len(negative) > 0:
                ans -= int("".join(negative))
                negative.clear()
            isNegative = c == '-'

    if len(negative) > 0:
        ans -= int("".join(negative))

    return ans


if __name__ == '__main__':
    # 输入获取
    s = input()

    # 算法调用
    print(getResult())
