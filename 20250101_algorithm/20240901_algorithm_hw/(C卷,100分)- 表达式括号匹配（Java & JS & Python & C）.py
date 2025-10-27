while True:
    try:
        str_b = ''.join([i for i in input() if i == '(' or i == ')'])
        count = 0
        while '()' in str_b:
            count += str_b.count('()')
            str_b = str_b.replace('()', '')
        print(count) if not str_b else print(-1)
    except:
        break
