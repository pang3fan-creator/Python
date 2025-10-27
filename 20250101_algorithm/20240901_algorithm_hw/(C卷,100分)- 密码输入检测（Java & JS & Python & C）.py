def judge_password(str_output):
    if len(str_output) < 8: return False
    a, b, c, d = False, False, False, False
    for item in str_output:
        if item.isupper():
            a = True
        elif item.islower():
            b = True
        elif item.isdigit():
            c = True
        else:
            d = True
    return a and b and c and d


def get_result():
    str_output = ''
    for item in str_input:
        if item == '<':
            str_output = str_output[0:-1:]
            continue
        str_output += item
    return str_output


if __name__ == '__main__':
    while True:
        try:
            str_input = input().strip()
            str_output = get_result()
            res = judge_password(str_output)
            print(f'{str_output},{str(res).lower()}')
        except:
            break
