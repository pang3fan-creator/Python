from multiprocessing import Process
import time


def read(str_temp, start_temp, end_temp):
    with open(f'./juwairen/局外人{start_temp}.txt', 'w') as f:
        f.write(str_temp[start_temp:end_temp:])


if __name__ == '__main__':
    num_info = int(input('请输入要拆分的个数：'))
    list_info = []
    start = time.time()
    with open('./局外人.txt', 'r') as file:
        str = file.read()
        txt_size = len(str)
        step = txt_size // num_info
        for start in range(0, txt_size, step):
            end = start + step if start + step < txt_size else txt_size
            my_Process = Process(target=read, args=(str, start, end))
            list_info.append(my_Process)
            my_Process.start()
    [i.join() for i in list_info]
    end = time.time()
    print(f'所有进程结束，总共耗时：{end - start}')
