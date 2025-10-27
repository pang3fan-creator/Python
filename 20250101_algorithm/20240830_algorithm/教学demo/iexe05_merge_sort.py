import random
import time


def merge_list(left_sorted, right_sorted):
    new_list = []
    while left_sorted and right_sorted:
        if left_sorted[0] < right_sorted[0]:
            new_list.append(left_sorted.pop(0))
        else:
            new_list.append(right_sorted.pop(0))
    if left_sorted:
        new_list.extend(left_sorted)
    if right_sorted:
        new_list.extend(right_sorted)
    return new_list


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge_list(left_sorted, right_sorted)


if __name__ == '__main__':
    random.seed(5)
    list = [i for i in range(1000)]
    random.shuffle(list)
    a = time.time()
    print(merge_sort(list))
    b = time.time()
    print(b - a)
