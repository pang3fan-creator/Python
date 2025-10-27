"""
程序随机产生1到100之间的随机数
让玩家反复猜，一直到猜对为止
大了  小了  猜了多少次，猜对了

"""
# 1. 引入库
import random

# 2. 产生随机数
random_number = random.randint(1, 100)
# print(random_number)

# 3. 核心代码
count = 0
while True:
    input_number = int(input("请输入数字："))
    count += 1
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print(f"猜对了，一共猜了{count}次")
        break
