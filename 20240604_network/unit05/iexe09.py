from threading import Lock, Thread


def num_print():
    for i in range(1, 53, 2):
        lock_1.acquire()
        print(i, i + 1)
        lock_2.release()


def char_print():
    for i in range(65, 91, 1):
        lock_2.acquire()
        print(chr(i))
        lock_1.release()


if __name__ == '__main__':
    lock_1 = Lock()
    lock_2 = Lock()
    my_thread_1 = Thread(target=num_print)
    my_thread_2 = Thread(target=char_print)
    lock_2.acquire()
    my_thread_1.start()
    my_thread_2.start()
    my_thread_1.join()
    my_thread_2.join()
    lock_2.release()
