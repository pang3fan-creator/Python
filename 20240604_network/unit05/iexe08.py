import time
from threading import Thread, Lock


def do_sell(window):
    while list_1:
        lock.acquire()
        print(f'{window}卖出第{list_1.pop(0)}')
        lock.release()
        time.sleep(0.01)


if __name__ == '__main__':
    list_1 = [f'{i}张票' for i in range(501)]
    lock = Lock()
    list_temp = []
    for i in range(1, 11, 1):
        my_thread = Thread(target=do_sell, args=(f'{i}号窗口',))
        list_temp.append(my_thread)
        my_thread.start()
    [i.join() for i in list_temp]
