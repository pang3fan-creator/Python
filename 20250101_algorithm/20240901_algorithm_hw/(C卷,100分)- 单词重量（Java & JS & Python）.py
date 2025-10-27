while True:
    try:
        # 输入获取
        arr = input().split()

        sumV = 0
        for i in range(len(arr)): sumV += len(arr[i])

        print(round(sumV / len(arr), 6))
    except:
        break
