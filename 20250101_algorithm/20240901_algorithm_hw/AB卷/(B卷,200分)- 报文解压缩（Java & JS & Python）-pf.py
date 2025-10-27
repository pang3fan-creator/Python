def main(str_input):
    list_num, list_str, list_output, index = [], [], [], 0

    for v in str_input:
        if v.isalpha(): list_str.append(v)
        if v.isdigit(): list_num.append(int(v))
        if v == '[':  index += 1
        if v == ']':
            index -= 1
            string = ''.join(list_str[index:]) * list_num.pop(-1)
            list_str = list_str[:index]
            list_output.append(string) if index == 0 else list_str.append(string)

    return ''.join(list_output)


if __name__ == '__main__':
    print(main(input().strip()))
