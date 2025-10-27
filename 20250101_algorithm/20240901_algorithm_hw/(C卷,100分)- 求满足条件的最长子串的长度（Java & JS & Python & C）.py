def get_result():
    list_str = []
    start, point, count = 0, 0, 0,
    for i in range(len(str_input)):
        if str_input[i].isalpha(): count += 1  # 判断是否为字母
        if count == 2:
            str_slice = str_input[start:i]
            list_str.append(str_slice) if len(str_slice) > 1 else None
            start, point, count = point + 1, i, count - 1
        if count == 1 and i == len(str_input) - 1:
            str_slice = str_input[start:]
            list_str.append(str_slice) if len(str_slice) > 1 else None
    return -1 if len(list_str) == 0 else max(map(len, list_str))


if __name__ == '__main__':
    str_input = input().strip()
    print(get_result())
