# 归并排序
import random


def merge_list(left_list, right_list):
    result = []  # 新列表
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] <= right_list[0]:  # 左侧列表头一个元素更小
            result.append(left_list.pop(0))
        else:
            result.append(right_list.pop(0))  # 弹出0号元素

    # 当子列表有剩余时，整体添加到result中
    if len(left_list) > 0:
        result.extend(left_list)
    if len(right_list) > 0:
        result.extend(right_list)

    return result


def merge_sort(list_target):
    if len(list_target) == 1:  # 递推出口：每个列表只有一个元素时停止递归
        return list_target

    # 拆分
    mid = len(list_target) // 2  # 整除
    left = list_target[0:mid]  # 取左半部分
    right = list_target[mid:]  # 取右半部分

    # 递归
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge_list(sorted_left, sorted_right)


if __name__ == "__main__":
    arr = []
    for i in range(99): arr.append(random.randint(0, 10000))

    sorted_list = merge_sort(arr)  # 执行归并排序
