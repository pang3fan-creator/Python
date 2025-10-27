# 快速排序
"""
1) 序列找一个参照值(哨兵值)，可以是随机取一个元素，可以是第一个元素
2) 从头、尾两个方向，依次取值和哨兵值比较，右侧值小于哨兵
   或左侧值大于哨兵值，左右侧指针值换位置
   迭代一轮哨兵值左侧的都是小于它的值，右侧都是大于它的值
3) 哨兵值左侧的部分、右侧部分进行递归调用，再做快速排序
"""
import random

count = 0  # 计数器


def quick_sort(arr, low, high):
    """
    快速排序
    :param arr: 待排序列表
    :param low: 排序起始位置
    :param high: 排序结束位置
    :return:
    """
    global count
    if len(arr) == 0 or len(arr) == 1:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]

    if low >= high:
        return

    k = arr[low]  # 哨兵值
    start = low  # 左侧指针
    end = high  # 右侧指针

    while start < end:
        while (start < end) and (arr[end] >= k):
            end -= 1  # 右侧指针向左移动
            count += 1
        arr[start] = arr[end]  # 右侧指针的值小于哨兵值，换位置

        while (start < end) and (arr[start] <= k):
            start += 1  # 左侧指针向右移动
            count += 1
        arr[end] = arr[start]  # 左侧指针的值大于哨兵值，换位置
    arr[start] = k  # 将哨兵值赋值到start位置

    quick_sort(arr, low, start - 1)  # 左侧递归
    quick_sort(arr, start + 1, high)  # 右侧递归


if __name__ == "__main__":
    arr = []
    N = 10000
    for i in range(N):  # 生成随机序列
        arr.append(random.randint(1, N))
    print(arr)  # 打印原始序列

    quick_sort(arr, 0, len(arr) - 1)  # 快速排序
    print(arr)  # 打印排序后序列
    print("比较次数：", count)
