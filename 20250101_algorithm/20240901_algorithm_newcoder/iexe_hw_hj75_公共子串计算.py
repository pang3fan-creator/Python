s1 = input()
s2 = input()

if len(s1) < len(s2):
    s1, s2 = s2, s1

res = 0
s = ''

for i in s2:
    s += i
    if s and s in s1:
        res = max(res, len(s))
    if s and s not in s1:  # 新增一个字符，s不是s1的子串了，但可能s[n:]为s1子串
        while s not in s1:
            s = s[1:]  # 从开始逐个清除字符直到s为s1子串或为''

print(res)
