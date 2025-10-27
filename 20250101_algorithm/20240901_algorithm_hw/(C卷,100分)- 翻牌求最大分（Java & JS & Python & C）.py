if __name__ == '__main__':
    # 输入获取
    arr = list(map(int, input().split(",")))
    n = len(arr)

    dp = [0] * n
    for i in range(n):
        if i == 0:
            dp[0] = max(0, arr[0])
        elif i < 3:
            dp[i] = max(0, dp[i - 1] + arr[i])
        else:
            dp[i] = max(dp[i - 3], dp[i - 1] + arr[i])
    print(dp[-1])
