from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, song):
        self._song = song
        # 1.在子类的构造函数调用父类的构造函数
        super().__init__()

    # 必须重写父类的run()方法,该方法不能存在返回值
    def run(self) -> None:
        for i in range(5):
            print('play', self._song)


mp = MyProcess('最炫风')
# Process类的start()方法
mp.start()
mp.join()
