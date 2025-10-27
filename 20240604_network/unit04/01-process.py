from multiprocessing import Process

from time import sleep


def func():
    print('start process')
    print('Son')
    sleep(3)
    print('process over')


# 创建(子)进程，并且指定需要完成的任务
p = Process(target=func)
# 启动进程
p.start()
# 回收进程

print('我也是进程')
sleep(2)
print('我也干活了')
p.join()
