list01 = [10, 20, 30]
for item in list01:
    print(item)
    item += 1
    print(item)
print(list01)

list02 = [
    [10],
    [20],
    [30],
]
for item in list02:
    item[0] += 1
print(list02)
