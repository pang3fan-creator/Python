import time

start = time.time()


def task(n):
    return n * n


list_1 = []
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    list_1.append(task(i))

print(list_1)
end = time.time()
print(end - start)
