if __name__ == '__main__':
    str_input = input().strip().split(',')
    str_output = ''
    for item in str_input:
        str_output += '/' + item.strip().replace('/', '') if item.strip() else ''
    if not str_output: str_output = '/'
    print(str_output)
