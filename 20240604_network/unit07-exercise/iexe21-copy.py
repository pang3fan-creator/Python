from multiprocessing import Process, Queue
import os


def copy(old, new, file):
    file_old = open(old + '/' + file, 'rb')
    file_new = open(new + '/' + file, 'wb')
    while True:
        data = file_old.read(1024)
        if not data:
            break
        file_new.write(data)
    file_old.close()
    file_new.close()
    queue.put(file)


def main(old, new):
    os.mkdir(new)
    jobs = []
    for file in os.listdir(old):
        p = Process(target=copy, args=(old, new, file))
        jobs.append(p)
        p.start()
    [job.join() for job in jobs]
    print('复制了以下文件')
    while queue.qsize():
        print(queue.get())


if __name__ == '__main__':
    old = input('请输入要复制的文件夹路径：')
    new = input('请输入要复制到的文件夹路径：')
    queue = Queue()
    main(old, new)
