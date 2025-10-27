from threading import Thread, Lock
from time import sleep


class MyThead(Thread):
    def __init__(self, song):
        self._song = song
        self.data = []
        self.lock = Lock()
        super().__init__()

    def run(self) -> None:
        for i in range(5):
            sleep(0.1)
            self.lock.acquire()
            self.data.append(i)
            print('I am sing', self._song)
            self.lock.release()


mt = MyThead('stronger')

mt.start()

mt.join()

print(mt.data)
