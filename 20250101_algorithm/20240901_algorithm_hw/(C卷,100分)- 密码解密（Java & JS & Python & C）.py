def get_result():
    i = len(str_input) - 1
    str_output = ''
    while i >= 0:
        if str_input[i] == '*':
            str_output = chr(int(str_input[i - 2:i]) + 96) + str_output
            i -= 3
            continue
        str_output = str_input[int(str_input[i]) + 96] + str_output
        i -= 1
    return str_output


if __name__ == '__main__':
    while True:
        try:
            str_input = input().strip().lower()
            print(get_result())
        except:
            break
