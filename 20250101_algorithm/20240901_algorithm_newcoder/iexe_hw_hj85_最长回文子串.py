"""
输入一个int类型数字
输出转成二进制之后连续1的个数
"""
while True:
    try:
        n = bin(int(input()))[2:]
        for i in range(len(n), 0, -1):
            if '1' * i in n:
                print(i)
                break
    except:
        break
