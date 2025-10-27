import time
from multiprocessing import Process, Queue


class MyProcess(Process, object):
    def __init__(self, start, end):
        super().__init__(daemon=False)
        self._start = start
        self._end = end

    def run(self) -> None:
        sum_num = 0
        for i in range(self._start, self._end, 1):
            sum_num += i
        queue.put(sum_num)


class MyCalculate(object):
    def __init__(self):
        self._start = int(input("请输入一个数字："))
        self._step = 100000 // self._start

    def calculate(self):
        list_1 = []
        for i in range(1, 100001, self._step):
            j = i + self._step if i + self._step <= 100001 else 100001
            process = MyProcess(*(i, j))
            list_1.append(process)
            process.start()
        [process.join() for process in list_1]

    def main(self):
        start = time.time()
        self.calculate()
        self.num_total()
        end = time.time()
        print(f"耗时：{end - start}")

    @staticmethod
    def num_total():
        num_total = 0
        while queue.qsize():
            num_total += queue.get()
        print(num_total)


if __name__ == '__main__':
    queue = Queue()
    MyCalculate().main()
    queue.close()
