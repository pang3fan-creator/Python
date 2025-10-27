def find_odd(list: list):
    for i in list:
        if i % 2 == 0:
            yield i


obj = find_odd([22, 33, 44, 55, 66, 77, 88, 99, 11, ])
print(type(obj))
print(obj)
for i in obj:
    print(i)
