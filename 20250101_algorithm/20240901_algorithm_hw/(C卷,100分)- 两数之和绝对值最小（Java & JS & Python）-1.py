import sys


def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) >> 1  # >> 1的作用是将整数除以2，相当于右移一位
        midVal = arr[mid]

        if midVal > target:
            high = mid - 1
        elif midVal < target:
            low = mid + 1
        else:
            return mid

    return -low - 1

    # 算法入口


def getResult():
    idx = binarySearch(nums, 0)
    if idx < 0:
        idx = -idx - 1

    # 全正数，或者 0+多个正数
    if idx == 0:
        return nums[0] + nums[1]

    n = len(nums)
    # 全负数，或者 多个负数+0
    if idx >= n - 1:
        return abs(nums[n - 2] + nums[n - 1])

    # 下面是有正有负的处理逻辑
    minV = sys.maxsize
    # maxsize是python的内置函数，返回一个整数，表示一个无符号整数的最大值，即2的31次方减1，也就是2147483647。

    # 负数部分最后两个值
    if idx >= 2:
        minV = min(minV, abs(nums[idx - 2] + nums[idx - 1]))

    # 非负数部分的前两个值
    if idx < n - 1:
        minV = min(minV, abs(nums[idx] + nums[idx + 1]))

    # 非负数部分的数组
    positive = nums[idx:]
    for i in range(0, idx):
        # 注意通过二分查找-nums[i]在positive的有序插入位置j，则最接近-nums[i]的值的位置有两个：j-1和j，其中j位置的元素值 >= -nums[i]，而j - 1位置的元素值 < -nums[i]
        j = binarySearch(positive, -nums[i])

        if j < 0:
            j = -j - 1

        if j == len(positive):
            j -= 1

        minV = min(minV, abs(nums[i] + positive[j]))

        if j - 1 >= 0: minV = min(minV, abs(nums[i] + positive[j - 1]))

    print(minV)


if __name__ == '__main__':
    # 输入获取
    nums = sorted(list(map(int, input().split())))

    # 算法调用
    print(getResult())
