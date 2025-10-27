import os
from multiprocessing import Process, Queue

# 消息队列
q = Queue()


# 进程函数  复制文件
def copy(old, new, file):
    fr = open(old + '/' + file, 'rb')
    fw = open(new + '/' + file, 'wb')
    while True:
        data = fr.read()
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()
    q.put(file)  # 存入队列


# 入口函数
def main(old):
    new = old.split('/')[-1]
    os.mkdir(new)  # 创建新文件夹
    jobs = []  # 存放每个进程对象
    # 循环创建进程 file --> 文件名称
    for file in os.listdir(old):
        p = Process(target=copy, args=(old, new, file))
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]  # 判断所有进程结束
    print("拷贝了如下文件:")
    while q.qsize():
        print(q.get())


if __name__ == '__main__':
    main("../images")
