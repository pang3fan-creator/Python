def get_result():
    if len(str_short) > len(str_long): return 'false'

    start, count = 0, 0
    for i in range(len(str_short)):
        for j in range(start, len(str_long)):
            if str_short[i] == str_long[j]:
                start, count = j + 1, count + 1
                break

    return 'true' if count == len(str_short) else 'false'


if __name__ == '__main__':
    str_short, str_long = input(), input()
    print(get_result())
