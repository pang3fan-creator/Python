# 算法入口
def getResult():
    cursor = len(target) - 1
    for i in range(len(source) - 1, -1, -1):
        if source[i] == target[cursor]:
            cursor -= 1
            if cursor < 0:
                return i

    return -1


if __name__ == '__main__':
    # 输入获取
    target = input()
    source = input()

    # 调用算法
    print(getResult())
