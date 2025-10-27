import sys, math

for line in sys.stdin:  # sys.stdin是用来读取输入的
    line = int(line)
    for i in range(2, int(math.sqrt(line)) + 1):
        while line % i == 0:
            print(i, end=" ")
            line = line // i
    if line > 2: print(line)
