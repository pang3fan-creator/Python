from multiprocessing import Process
from time import sleep


class MyProcess(Process):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def run(self):
        for i in range(int(self.value)):
            sleep(0.5)
            print('自定义进程%d' % i)


if __name__ == '__main__':
    p = MyProcess(5)
    p.start()
    p.join()
