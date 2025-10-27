def get_result():
    arr_length = len(arr)
    if arr_length <= 3: return -1
    max_length = 0
    for i in range(arr_length):
        str_temp = arr[i % arr_length] + 'o' + arr[(i + 1) % arr_length] + 'o' + arr[(i + 2) % arr_length]
        max_length = max(max_length, len(str_temp))
    return max_length


if __name__ == '__main__':
    arr = input().strip().split('o')
    print(get_result())
