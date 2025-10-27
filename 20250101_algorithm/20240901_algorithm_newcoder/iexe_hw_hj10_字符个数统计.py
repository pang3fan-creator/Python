import sys

a = sys.stdin.readline().strip()

words = ''
for i in a:
    if i not in words and ord(i) >= 0 and ord(i) <= 127:
        words += i
print(len(words))
