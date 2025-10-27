from multiprocessing import Process


class SonProcess(Process, object):
    def __init__(self, name, daemon):
        super().__init__(daemon=daemon)
        self._name = name

    def run(self) -> None:
        for i in range(5):
            print("子进程%s" % self._name)


a=SonProcess("子进程1", False)
a.start()

print("父进程")
