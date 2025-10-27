from multiprocessing import Process

from time import  sleep


def func():
    print('我是子进程')
    sleep(2)
    print('子进程结束了')

if __name__ == '__main__':

    p = Process(target= func)
    # 启动进程
    p.start()
    sleep(2)
    p.join()
    print('我是父进程')
    print('父进程也结束了')



