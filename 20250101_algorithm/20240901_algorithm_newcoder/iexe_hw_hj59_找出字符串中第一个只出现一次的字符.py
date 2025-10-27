"""
输入一个非空字符串
输出第一个只出现一次的字符，如果不存在输出-1
"""

line = input().strip()
dict_line = {}
for i in line:
    dict_line.setdefault(i, 0)
    dict_line[i] += 1
list_line = [i for i, v in dict_line.items() if v == 1]
result = list_line[0].strip() if list_line else -1
print(result)
