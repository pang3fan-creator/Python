def get_result():
    str_output = list_input.pop(0)
    str_input = ''.join(list_input)
    i = 0
    while i <= len(str_input) - 1:
        str_output, i = str_output + '-' + str_input[i:i + N:], N + i
    return str_output.upper()


if __name__ == '__main__':
    N = int(input())
    list_input = input().strip().split('-')
    print(get_result())
