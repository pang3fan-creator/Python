from multiprocessing import Process, Pool
import time


class Prime(Process):
    def __init__(self, begin, end):
        self.value = begin
        self.end = end
        super().__init__()

    def run(self):
        prime = []
        for i in range(self.value, self.end):
            if self.is_prime(i):
                prime.append(i)
        prime.sort(reverse=True)
        print(sum(prime))

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    jobs = []
    start = time.time()
    for i in range(1, 100001, 10000):
        p = Prime(i, i + 10000)
        jobs.append(p)
        p.start()
    [job.join() for job in jobs]
    end = time.time()
    print(end - start)
