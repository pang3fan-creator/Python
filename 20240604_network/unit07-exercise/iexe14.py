from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print('%s is working...' % name)


my_process = Process(target=worker, args=(2, 'tom'))
my_process.start()
print('子进程pid：%d' % my_process.pid)
my_process.join()
