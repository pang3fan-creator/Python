# 算法入口
def getResult():
    correct = 0
    for i in range(len(arr)):
        fault = arr[i]
        if fault > 4:
            fault -= 1

        for j in range(len(arr) - i - 1, 0, -1):
            fault *= 9

        correct += fault
    return correct


if __name__ == '__main__':
    # 输入获取
    arr = list(map(int, list(input())))

    # 调用算法
    print(getResult())
