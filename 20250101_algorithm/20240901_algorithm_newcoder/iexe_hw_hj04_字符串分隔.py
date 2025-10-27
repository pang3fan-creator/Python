import sys

s = input()
if len(s) % 8 != 0:
    s += '0' * (8 - len(s) % 8)

for i in range(len(s) // 8):
    print(s[8 * i:8 * i + 8], sep='')
