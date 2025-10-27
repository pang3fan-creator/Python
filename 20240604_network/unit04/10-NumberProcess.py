from multiprocessing import Process, Queue

from time import time


class NumberProcess(Process):

    def __init__(self, start, end, q):
        self._start = start
        self._end = end
        self._q = q
        super().__init__()

    # 让每个进程执行的业务代码
    def run(self) -> None:
        sum = 0
        for i in range(self._start, self._end):
            sum += i
        # 将当前进程的运算结果存储到队列
        self._q.put(sum)


if __name__ == '__main__':

    start_time = time()

    # 创建对列对象
    q = Queue()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # 通过不同的进程数量来演示：进程并非越多运行效率运高

    # 进程数量
    n = 9

    # 步长
    step = 100 // n

    # 用于存储进程ID
    jobs = []

    for i in range(1, 101, step):
        stop = i + step
        if stop >= 101:
            stop = 101
        np = NumberProcess(i, stop, q)
        jobs.append(np)
        np.start()

    end_time = time()

    print('共花费了', (end_time - start_time))

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    ################################################

    [job.join() for job in jobs]

    # 进程间的通信

    result = []
    # qsize()方法用于获取队列成员的数量，其为动态值
    while q.qsize():
        result.append(q.get())

    print(sum(result))

################################################
