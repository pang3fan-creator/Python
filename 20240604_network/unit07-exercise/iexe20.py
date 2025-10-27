from multiprocessing import Process, Queue


def handle():
    while True:
        cmd = q.get()
        if cmd == '1':
            print('1')
        elif cmd == '2':
            print('2')
        else:
            print('其他数')


if __name__ == '__main__':
    q = Queue()
    p = Process(target=handle, daemon=True)
    p.start()
    while True:
        cmd = input('>>>')
        if not cmd:
            break
        q.put(cmd)
    p.join()
