import time
from threading import Thread


def decorate(func):
    def wrapper(args):
        start = time.time()
        func(args)
        end = time.time()
        print(end - start)

    return wrapper


class MyThread(Thread, object):
    def __init__(self, song):
        super().__init__()
        self._song = song

    @decorate
    def run(self) -> None:
        for i in range(1, 51):
            time.sleep(0.1)
            print('播放歌曲', self._song, i)


myt1 = MyThread('凉凉')
myt1.run()
