import time
from multiprocessing import Pool

start = time.time()


def task(n):
    return n * n


with Pool(4) as p:
    results = p.map(task, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(results)
end = time.time()
print(end - start)
