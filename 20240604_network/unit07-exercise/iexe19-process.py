from multiprocessing import Pool, Queue
import time


def run(start, end):
    for i in range(start, end):
        if is_prime(i):
            queue.put(i)
            print(i)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    queue = Queue()
    start = time.time()
    pool = Pool(10)
    for i in range(1, 10001, 500):
        pool.apply_async(run, args=(i, i + 500))
    list_temp = []
    while True:
        try:
            list_temp.append(queue.get(timeout=1))
        except:
            break
    list_temp.sort()
    print(list_temp)
    print(sum(list_temp))
    pool.close()
    queue.close()
    end = time.time()
    print(end - start)
