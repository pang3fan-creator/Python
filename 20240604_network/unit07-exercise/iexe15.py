from multiprocessing import Process
from time import sleep
import sys, os


def th_1():
    sleep(3)
    print("子进程1")
    print(os.getppid(), os.getpid())


def th_2():
    sleep(3)
    print("子进程2")
    print(os.getppid(), os.getpid())


def th_3():
    sleep(3)
    print("子进程3")
    print(os.getppid(), os.getpid())


jobs = []
for i in [th_1, th_2, th_3]:
    p = Process(target=i)
    jobs.append(p)
    p.start()
[job.join() for job in jobs]
