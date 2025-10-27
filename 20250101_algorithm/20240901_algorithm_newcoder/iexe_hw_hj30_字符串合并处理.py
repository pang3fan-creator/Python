hex_num = ['0', '1', '2', '3',
           '4', '5', '6', '7',
           '8', '9', 'a', 'b',
           'c', 'd', 'e', 'f',
           'A', 'B', 'C', 'D',
           'E', 'F']


def helper(s):
    ten = int(s, 16)
    bc = format(ten, 'b').rjust(4, '0')
    bc = list(bc)
    bc.reverse()
    ten = int(''.join(bc), 2)
    hc = format(ten, 'x')
    return hc.upper()


while True:
    try:
        a, b = input().strip().split()
        res = list(a + b)
        res[::2] = sorted(res[::2])
        res[1::2] = sorted(res[1::2])
        for i in range(len(res)):
            if res[i] in hex_num:
                res[i] = helper(res[i])
        print(''.join(res))
    except EOFError:
        break
