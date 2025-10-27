import sys



a_type = [1 << 24, (127 << 24) - 1]
b_type = [128 << 24, (192 << 24) - 1]
c_type = [192 << 24, (224 << 24) - 1]
d_type = [224 << 24, (240 << 24) - 1]
e_type = [240 << 24, (1 << 32) - 1]

p1 = [10 << 24, (11 << 24) - 1]
p2 = [(172 << 24) + (16 << 16), (172 << 24) + (32 << 16) - 1]
p3 = [(192 << 24) + (168 << 16), (192 << 24) + (169 << 16) - 1]


def parse_mask(mask):
    chunks = mask.split('.')
    if len(chunks) != 4:
        return 1
    val = 0
    for c in chunks:
        if len(c) == 0:
            return 1
        val = val * 256 + int(c)
    if val == 0 or val == 0xffffffff:
        return 1
    prev = 0
    while val > 0:
        cur = val & 1
        if cur == 0 and prev == 1:
            return 1
        prev = cur
        val = (val >> 1)
    return 0


def parse_addr(addr):
    chunks = addr.split('.')
    if len(chunks) != 4:
        return (5, 0)
    val = 0
    for c in chunks:
        if len(c) == 0:
            return (5, 0)
        val = val * 256 + int(c)
    if val >= a_type[0] and val <= a_type[1]:
        if val >= p1[0] and val <= p1[1]:
            return (0, 1)
        else:
            return (0, 0)
    if val >= b_type[0] and val <= b_type[1]:
        if val >= p2[0] and val <= p2[1]:
            return (1, 1)
        else:
            return (1, 0)
    if val >= c_type[0] and val <= c_type[1]:
        if val >= p3[0] and val <= p3[1]:
            return (2, 1)
        else:
            return (2, 0)
    if val >= d_type[0] and val <= d_type[1]:
        return (3,0)
    if val >= e_type[0] and val <= e_type[1]:
        return (4, 0)

    return (-1, 0)




# A, B, C, D, E, error, private,
cnts = [0, 0, 0, 0, 0, 0, 0]

for line in sys.stdin.readlines():
    (addr, mask) = line.strip().split('~')
    (t, p) = parse_addr(addr)
    c = parse_mask(mask)
    if c == 1 and t != -1:
        cnts[5] += 1
    elif t >= 0:
        cnts[t] += 1
        if p > 0:
            cnts[6] += 1

cnts = [str(x) for x in cnts]
print(' '.join(cnts))







