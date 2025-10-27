from threading import Thread, Lock
import time

lock = Lock()

ticket = ["T%d" % x for x in range(1, 501)]


def sell(w):
    while ticket:
        lock.acquire()
        print("%s --- %s" % (w, ticket.pop(0)))
        lock.release()
        time.sleep(0.01)



list_1 = []
for i in range(1, 11):
    t = Thread(target=sell, args=("W%d" % i,))
    list_1.append(t)
    t.start()
[t.join() for t in list_1]
