from multiprocessing import Process
from time import sleep


def eat():
    print('eating')
    sleep(2)


def sleeping():
    print('sleeping')
    sleep(2)


def study():
    print('study')
    sleep(1)


jobs = []
# 遍历由执行的任务所组成的列表,依次将任务让进程执行
for fun in [eat, sleeping, study]:
    p = Process(target=fun)
    # p1 = Process(target=eag)
    # p2 = Process(target=sleeping)
    # p3 = Process(target=study)
    jobs.append(p)
    p.start()

# 进程的回收
[job.join() for job in jobs]
