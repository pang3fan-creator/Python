from multiprocessing import Process
from time import sleep


def func():
    print('SON')
    sleep(2)
    print('over')


p1 = Process(target=func, daemon=True)

p1.start()

print('I am parent')

p1.join(5)


