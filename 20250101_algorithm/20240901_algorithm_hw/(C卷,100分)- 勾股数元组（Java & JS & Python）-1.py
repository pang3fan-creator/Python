import math
import time

# 输入获取
n = int(input())
m = int(input())


# 判断两个数是否互质，辗转相除
def isRelativePrime(x, y):
    while y > 0:
        mod = x % y
        x = y
        y = mod

    return x == 1


# 算法入口
def getResult():
    arr = []

    for i in range(n, m + 1):
        arr.append(i * i)

    setArr = set(arr)

    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # 判断勾股数 a^2 + b^2 = c^2
            sumV = arr[i] + arr[j]
            if sumV in setArr:
                res.append([int(math.sqrt(arr[i])), int(math.sqrt(arr[j])), int(math.sqrt(sumV))])

    ans = list(
        filter(lambda x: isRelativePrime(x[0], x[1]) and isRelativePrime(x[0], x[2]) and isRelativePrime(x[1], x[2]),
               res))

    if len(ans) == 0:
        print("NA")
    else:
        for g in ans:
            print(" ".join(map(str, g)))


# 算法调用
a = time.time()
getResult()
b = time.time()
print(b - a)
