import time
from multiprocessing import Process


def func1():
    print('func1')
    time.sleep(2)


def func2():
    print('func2')
    time.sleep(1)


def func3():
    print('func3')
    time.sleep(1)


func_list = [func1, func2, func3]
func_list2 = []
for func in func_list:
    p = Process(target=func)
    func_list2.append(p)
    p.start()
[func.join() for func in func_list2]
