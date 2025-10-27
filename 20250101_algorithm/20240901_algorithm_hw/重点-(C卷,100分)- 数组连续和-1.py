# 算法入口
def getResult():
    preSum = [0] * (n + 1)

    for i in range(1, n + 1): preSum[i] = preSum[i - 1] + arr[i - 1]

    l = 0
    r = 1
    ans = 0

    while r <= n:
        if preSum[r] - preSum[l] >= x:
            ans += n - r + 1
            l += 1
            r = l + 1
        else:
            r += 1

    return ans


if __name__ == '__main__':
    # 输入获取
    n, x = map(int, input().split())
    arr = list(map(int, input().strip().split(' ')))

    # 算法调用
    print(getResult())
