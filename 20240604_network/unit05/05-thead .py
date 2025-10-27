from threading import Thread
import time


def func():
    global a
    a = 666
    print('I am thread')
    print('I am thread variable a', a)
    for _ in range(3):
        time.sleep(2)
        print('Play Music')


a = 1
# 创建线程并且指定线程需要执行的函数
t = Thread(target=func)
t.start()
t.join()
print('I am process')
print('I am process varaible a:', a)
