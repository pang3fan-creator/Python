# 牌大小 映射为 数值
def cards(num):
    if num == "J":
        return 11
    elif num == "Q":
        return 12
    elif num == "K":
        return 13
    elif num == "A":
        return 14
    else:
        return int(num)


def countNums(nums, partCount, maxSameNumCount):
    count = {}

    for num in nums:  count[num] = count.get(num, 0) + 1
    if len(count.keys()) != partCount: return False

    return maxSameNumCount in count.values()


# 三条
def isSantiao(nums):
    # 三条由三部分组成，第一个部分由三张相同牌组成，第二个，第三个部分分别是两种不同的牌
    return countNums(nums, 3, 3)


# 葫芦
def isHulu(nums):
    # 葫芦由两部分组成，一个部分三张牌相同，一个部分两张牌相同
    return countNums(nums, 2, 3)


# 四条
def isSitiao(nums):
    # 四条由两部分组成，一个部分四张相同牌，一个部分一张牌
    return countNums(nums, 2, 4)


# 同花
def isTonghua(colors):
    # 同花牌的所有花色都一样
    return len(set(colors)) == 1


# 顺子
def isShunzi(nums):
    if "".join(nums) == "2345A": return True

    for i in range(1, len(nums)):
        if cards(nums[i - 1]) + 1 != cards(nums[i]): return False
    return True


if __name__ == '__main__':
    # 输入获取
    arr = [input().split() for _ in range(5)]
    nums = [item[0] for item in arr]
    nums.sort(key=lambda x: cards(x))
    colors = [item[1] for item in arr]

    if isShunzi(nums) and isTonghua(colors):
        print(1)
    elif isSitiao(nums):
        print(2)
    elif isHulu(nums):
        print(3)
    elif isTonghua(colors):
        print(4)
    elif isShunzi(nums):
        print(5)
    elif isSantiao(nums):
        print(6)
    else:
        print(0)
