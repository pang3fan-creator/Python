# 输入获取
n = int(input())
k = int(input())
arr = [i + 1 for i in range(n)]

fact = [0] * (n + 1)
fact[1] = 1
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i


# 算法入口
def getResult(n, k, arr):
    if n == 1:
        return "1"

    f = fact[n - 1]
    prefix = arr[(k - 1) // f]
    k %= f
    k = f if k == 0 else k

    arr = list(filter(lambda x: x != prefix, arr))

    if k == 1:
        return str(prefix) + "".join(map(str, arr))
    else:
        return str(prefix) + getResult(n - 1, k, arr)


# 算法调用
print(getResult(n, k, arr))
