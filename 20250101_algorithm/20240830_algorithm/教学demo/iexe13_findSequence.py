import math
import time
if __name__ == '__main__':
    N = int(input("请输入用于求取数列的整数："))
    N_max = (N - 1) // 2
    list_n = []
    t1=time.time()
    for i in range(1, N_max + 1):
        sum_n = 0
        list_temp = []
        num = int(math.sqrt(2 * N + i * i - i + 0.25) - 0.5)
        for j in range(i, num + 1):
            sum_n += j
            list_temp.append(j)
            if sum_n == N:
                list_n.append(list_temp)
                break
        del list_temp
    t2=time.time()
    print(list_n)
    print(t2-t1)
