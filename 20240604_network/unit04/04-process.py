from multiprocessing import  Process

# 进程之间相互独立，互不影响
def func():
    # 访问的是子进程内存空间的变量 a
    global a
    a = 666
    print(a)


a = 1

p = Process(target=func)

p.start()

# 访问的是父进程内存空间的变量 a
print(a)

p.join()