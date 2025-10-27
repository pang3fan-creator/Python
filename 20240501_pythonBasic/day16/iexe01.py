"""
zip()
"""
list_1 = ['1-', '2-', '3-', '4-', '5-']
list_2 = [6, 7, 8, 9, 10, 11]
dict_1 = dict(zip(list_1, list_2))
print(type(dict_1))
print(dict_1)

for i in zip(list_1, list_2):
    item = {i[0]: i[1]}
    print(item)
list_map = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]
list_new = (list(i) for i in zip(*list_map))

print(type(list_new))
for i in list_new:
    print(i)
for i in list_new:
    print(i)

list1 = ['老赵', '老王', '老刘']
list2 = ['25', '28', '30']

list3 = dict([i for i in zip(list1, list2)])
print(list3)
