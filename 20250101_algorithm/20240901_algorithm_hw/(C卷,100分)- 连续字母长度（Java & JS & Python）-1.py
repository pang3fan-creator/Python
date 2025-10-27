# 算法入口
def getResult():
    global s
    global k

    if k <= 0:
        return -1

    s += "0"

    count = {}

    b = s[0]
    long = 1

    for i in range(1, len(s)):
        c = s[i]

        if b == c:
            long += 1
        else:
            if count.get(b) is None or count[b] < long:
                count[b] = long
            long = 1
            b = c

    arr = list(count.values())

    if k > len(arr):
        return -1
    else:
        arr.sort(reverse=True)
        return arr[k - 1]


if __name__ == '__main__':
    # 输入获取
    s = input()
    k = int(input())

    # 算法调用
    print(getResult())
