m = int(input())
requirements = list(map(int, input().split()))


def check(limit):
    l = 0
    r = len(requirements) - 1

    need = 0

    while l <= r:
        if requirements[l] + requirements[r] <= limit:
            l += 1
        r -= 1

        need += 1

    return m >= need


def getResult():
    requirements.sort()

    low = requirements[-1]
    high = requirements[-2] + requirements[-1]

    ans = high

    while low <= high:
        mid = (low + high) >> 1

        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


print(getResult())
