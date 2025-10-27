from threading import Thread, Lock


def print_num():
    for i in range(1, 53, 2):
        # 启用数字锁
        num_lock.acquire()
        print(i, i + 1)
        # 释放字符锁
        char_lock.release()


def print_char():
    for i in range(65, 91):
        # 启用字符锁
        char_lock.acquire()
        print(chr(i))
        # 释放数字锁
        num_lock.release()


# 创建字符锁
char_lock = Lock()
# 创建数字锁
num_lock = Lock()

num_thread = Thread(target=print_num)
char_thread = Thread(target=print_char)

# 启用字符锁
char_lock.acquire()
char_thread.start()

num_thread.start()

num_thread.join()
char_thread.join()

for char in 'ABCDE':
    print(ord(char))
