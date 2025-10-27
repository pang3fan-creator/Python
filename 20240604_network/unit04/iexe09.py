import time
from multiprocessing import Process, Queue


class SonProcess(Process, object):
    def __init__(self, start, end, daemon):
        self._start = start
        self._end = end
        super(SonProcess, self).__init__(daemon=daemon)

    def run(self) -> None:
        sum_1 = 0
        for i in range(self._start, self._end + 1, 1):
            sum_1 += i
        q.put(sum_1)
        print(sum_1)


def decorate(args):
    def wrapper():
        a = time.time()
        args()
        print(time.time() - a)

    return wrapper


@decorate
def calculate():
    list_1 = []
    for i in range(1, 100000, 50000):
        m = i + 50000 if i + 50000 < 100000 else 100000
        p = SonProcess(i, m, False)
        list_1.append(p)
        p.start()
    [i.join() for i in list_1]
    sum_total = sum(q.get() for i in range(q.qsize() - 1, -1, -1))
    print(sum_total)


if __name__ == '__main__':
    q = Queue()
    calculate()
