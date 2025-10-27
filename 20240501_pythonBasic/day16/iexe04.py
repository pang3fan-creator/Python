list_num = [11, 82, 73, 54, 65, 76, 97, 98, 19, 210]


def find_div(num):
    return num % 3 == 0 or num % 5 == 0


def find_odd(num):
    return num % 2 != 0


def find_num(function, numbers):
    for num in numbers:
        if function(num):  # num % 2 != 0   num % 3 == 0 or num % 5 == 0
            yield num


find_1 = find_num(find_div, list_num)
for i in find_1:
    print(i)
print()
find_2 = find_num(find_odd, list_num)
for i in find_2:
    print(i)
