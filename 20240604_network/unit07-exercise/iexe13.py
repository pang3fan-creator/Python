import multiprocessing as mp
import time

a = 1


def fun():
    print('look，a new start')
    time.sleep(2)
    global a
    print('a=', a)
    a = 10000
    print('a=', a)


process = mp.Process(target=fun)
process.start()
print('look，a old start')
print('a=', a)
process.join()
