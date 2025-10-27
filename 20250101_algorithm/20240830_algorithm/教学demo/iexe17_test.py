def get_result():
    str_num, str_str = '', ''
    for i in range(len(str_input) - 1):
        if str_input[i].isalpha():
            str_num = str_num + str_input[i] if str_input[i + 1].isalpha() else str_num + str_input[i] + ' '
        if str_input[i].isdigit():
            str_str = str_str + str_input[i] if str_input[i + 1].isdigit() else str_str + str_input[i] + ' '
    if str_input[-1].isalpha():
        str_num = str_num + str_input[-1]
    else:
        str_str = str_str + str_input[-1]
    list_num = sorted(map(int, str_str.strip().split(' ')))
    list_str = sorted(str_num.strip().split(' '))
    print(list_num), print(list_str)


if __name__ == '__main__':
    str_input = input("请输入一个字符串：")
    get_result()
