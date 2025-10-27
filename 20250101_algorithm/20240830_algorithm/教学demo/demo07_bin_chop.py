# 二分查找
def binary_chop(lst, to_find, start, end):
    print("start:", start, "end:", end)
    if start > end:
        return -1

    mid = (end + start) // 2  # 取中间元素索引值

    if lst[mid] == to_find:
        return mid
    elif lst[mid] > to_find:  # 中间的元素比要查找的值大
        end = mid - 1
        return binary_chop(lst, to_find, start, end)
    else:  # lst[mid] < to_find:   中间的元素比要查找的值小
        start = mid + 1
        return binary_chop(lst, to_find, start, end)


lst = []
for i in range(100):
    lst.append(i)

# lst = [1, 2, 4, 6, 8, 9, 11, 13, 14, 15, 17, 19, 20,22]
print(lst)
pos = binary_chop(lst, 22, 0, len(lst) - 1)
print(pos)
