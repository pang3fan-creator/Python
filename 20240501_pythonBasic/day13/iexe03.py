list_1 = [1, 2, 5, 4, 3]
list_2 = [6, 7, 8, 9, 10, 10, 10, 10]
list_1.sort(reverse=True)
print(list_1)
list_1.sort()
print(list_1)
list_1.extend(list_2)
print(list_1)
set_1 = set(list_1)
print(set_1)
str_1 = str(set_1)
a = 1
b = 2
a,b=b,a
