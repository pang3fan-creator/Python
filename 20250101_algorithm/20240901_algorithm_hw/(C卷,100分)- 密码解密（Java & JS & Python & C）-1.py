# 输入获取
s = input()

for i in range(26, 0, -1):
    key = str(i)
    if i > 9: key += "*"

    val = chr(97 + i - 1)

    s = s.replace(key, val)

print(s)
