a = input()
a = a[::-1]
y = ''
for i in a:
    if i not in y:
        y = y + i
print(y)
