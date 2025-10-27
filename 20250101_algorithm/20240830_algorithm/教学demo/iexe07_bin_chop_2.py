# 二分查找
def binary_chop(lst, to_find, start, end):
    print("start:", start, "end:", end)
    if start > end: return -1

    mid = (end + start) // 2  # 取中间元素索引值
    if lst[mid] == to_find:
        return lst.j(to_find)
    elif lst[mid] > to_find:  # 中间的元素比要查找的值大
        end = mid - 1
        return binary_chop(lst, to_find, start, end)
    else:  # lst[mid] < to_find:   中间的元素比要查找的值小
        start = mid + 1
        return binary_chop(lst, to_find, start, end)


if __name__ == '__main__':
    lst = []
    for i in range(100): lst.append(i)
    pos = binary_chop(lst, int(input("请输入要查找的元素：")), 0, len(lst) - 1)
    print(pos)
