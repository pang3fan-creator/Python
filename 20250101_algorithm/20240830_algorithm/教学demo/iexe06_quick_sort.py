import random


def quick_sort(arr, low, high):
    if len(arr) == 0 or len(arr) == 1: return arr
    if len(arr) == 2: return [arr[1], arr[0]] if arr[0] > arr[1] else arr
    if low >= high: return -1

    k = arr[low]  # 哨兵值
    start = low  # 左侧指针
    end = high  # 右侧指针

    while start < end:
        while (start < end) and (arr[end] >= k): end -= 1  # 右侧指针向左移动
        arr[start] = arr[end]  # 右侧指针的值小于哨兵值，换位置
        while (start < end) and (arr[start] <= k): start += 1  # 左侧指针向右移动
        arr[end] = arr[start]  # 左侧指针的值大于哨兵值，换位置
    arr[start] = k  # 将哨兵值赋值到start位置

    quick_sort(arr, low, start - 1)  # 左侧递归
    quick_sort(arr, start + 1, high)  # 右侧递归


if __name__ == '__main__':
    random.seed(5)
    list = [i for i in range(1000)]
    random.shuffle(list)
    quick_sort(list, 0, len(list) - 1)
    print(list)
