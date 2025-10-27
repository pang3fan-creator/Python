'''
基于python代码实现感知机
'''


def AND(x1, x2):
    w1, w2 = 0.5, 0.5
    theta = 0.7

    temp = x1 * w1 + x2 * w2
    if temp > theta:
        return 1
    else:
        return 0


# print(AND(1,1)) #1
# print(AND(1,0)) #0
# print(AND(0,1)) #0
# print(AND(0,0)) #0


def OR(x1, x2):
    w1, w2 = 0.5, 0.5
    theta = 0.3

    temp = x1 * w1 + x2 * w2
    if temp > theta:
        return 1
    else:
        return 0


# print(OR(1,1)) #1
# print(OR(1,0)) #1
# print(OR(0,1)) #1
# print(OR(0,0)) #0


def XOR(x1, x2):
    s1 = not AND(x1, x2)
    s2 = OR(x1, x2)
    res = AND(s1, s2)
    return res


print(XOR(1, 1))  # 0
print(XOR(1, 0))  # 1
print(XOR(0, 1))  # 1
print(XOR(0, 0))  # 0
