def get_result():
    global str_input
    count = str_input.count('1,1,1')
    str_input = str_input.replace('1,1,1', '')
    count += str_input.count('1,1')
    str_input = str_input.replace('1,1', '')
    count += str_input.count('1')
    return count


if __name__ == '__main__':
    str_input = input().strip()
    print(get_result())
