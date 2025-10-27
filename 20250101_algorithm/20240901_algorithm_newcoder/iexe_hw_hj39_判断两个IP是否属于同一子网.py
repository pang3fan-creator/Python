import sys


def is_valid_ip(s):
    s = [int(i) for i in s]
    if len(s) != 4:
        return False
    if s[0] == '0':
        return False
    for i in s:
        if i < 0 or i > 255:
            return False
    return True


def is_valid_mask(s):
    a = []
    # print(s)
    for i in s:
        i = int(i)
        if i < 0 or i > 256:
            return False
        else:
            x = str(bin(i)).split('b')[1]
            if len(x) < 8:
                x = '0' * (8 - len(x)) + x
            a.append(x)
    # print(a)
    s = ''.join(a)
    # print(s)
    if len(s) != 32:
        return False
    if s[0] == '0':
        return False
    o = False
    for i in s:
        if i == '0':
            o = True
        if i == '1' and o:
            return False
    return True


while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    mask = line.split('.')
    ip1 = sys.stdin.readline().strip().split('.')
    ip2 = sys.stdin.readline().strip().split('.')
    if not is_valid_mask(mask) or \
            not is_valid_ip(ip1) or not is_valid_ip(ip2):
        print(1)
        continue
    count = 0
    for i in range(len(mask)):
        a = int(ip1[i]) & int(mask[i])
        b = int(ip2[i]) & int(mask[i])
        if (a == b):
            count += 1
    if count == len(mask):
        print(0)
    else:
        print(2)
