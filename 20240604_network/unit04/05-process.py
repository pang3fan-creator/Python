import os
from multiprocessing import Process
from time import sleep


def func(name, secs):
    print('当前进程的ID号是', os.getpid())
    print('父进程的ID号是', os.getppid())
    print('I am', name)
    for i in range(3):
        print(name, 'say:I am working', i)
        sleep(secs)
    print('work finished')


# 位置参数，必须为元组
p1 = Process(target=func, args=('Tom', 1))
# 关键字参数，必须为字典
p2 = Process(target=func, kwargs={'name': 'Rose', 'secs': 1})
# 混合写法,实践中不允许
p3 = Process(target=func, args=('Frank',), kwargs={'secs': 1})

p1.start()
p2.start()
p3.start()

print('父进程的ID号是', os.getpid())

p1.join()
p2.join()
p3.join()
