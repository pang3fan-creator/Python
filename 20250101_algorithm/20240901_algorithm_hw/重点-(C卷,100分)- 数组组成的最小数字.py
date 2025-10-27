import functools

# 输入获取
strs = input().split(",")


# 算法入口
def cmp(a, b):
    s1 = a + b
    s2 = b + a
    return 0 if s1 == s2 else 1 if s1 > s2 else -1


def getResult(strs):
    strs.sort(key=lambda x: int(x))
    tmp = strs[:3]
    tmp.sort(key=functools.cmp_to_key(cmp))
    return "".join(tmp)


# 算法调用
print(getResult(strs))
