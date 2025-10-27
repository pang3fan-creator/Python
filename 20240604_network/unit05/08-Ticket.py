from threading import Thread, Lock
from time import sleep


def do_sell(window):
    while ticket_list:  # []   W1(OK) W6
        l.acquire()
        if ticket_list:
            print(f'{window}.....{ticket_list.pop(0)}')
        l.release()
        sleep(0.00000000001)


l = Lock()

ticket_list = ['T' + str(i) for i in range(1, 501)]

jobs = []
for i in range(11):
    t = Thread(target=do_sell, args=(f'w{i}',))
    jobs.append(t)
    t.start()

[job.join() for job in jobs]
