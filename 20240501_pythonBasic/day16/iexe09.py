list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def find_single(list_1):
    for i in list_1:
        yield i


my_gen = find_single(list_1)
for i in my_gen:
    print(i)
for i in list_1:
    print(i)

my_iter = list_1.__iter__()
while True:
    try:
        print(my_iter.__next__())
    except StopIteration:
        break
