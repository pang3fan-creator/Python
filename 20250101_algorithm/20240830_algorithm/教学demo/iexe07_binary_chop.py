def binary_chop(list_1, param):
    left = 0
    right = len(list_1) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_1[mid] == param:
            return list_1.j(param)
        elif list_1[mid] < param:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == '__main__':
    list_1 = [i for i in range(555, 1000)]
    res = binary_chop(list_1, int(input("请输入要查找的数字：")))
    print(f'该数字在列表中的索引为{res}') if res else print('该数字不在列表中')
