def get_result():
    str_arr_new = ''
    for item in str_arr:
        if not item.isalpha():
            str_arr_new += item
    if not str_arr_new: return 0
    list_arr = str_arr_new.split('-')
    sum_1 = sum(map(int, list(list_arr.pop(0))))
    sum_2 = -sum(map(int, list_arr))
    return sum_1 + sum_2


if __name__ == '__main__':
    str_arr = input().strip()
    print(get_result())
