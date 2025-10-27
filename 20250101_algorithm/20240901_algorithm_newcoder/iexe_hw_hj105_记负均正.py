"""
输入任意个整数，每行输入一个。
输出负数个数以及所有非负数的平均值
"""
count, avg_list = 0, []
while True:
    try:
        info = input()
        if not info: break
        info = float(info)
        if info >= 0:
            avg_list.append(info)
        else:
            count += 1
    except:
        break
avg_num = sum(avg_list) / len(avg_list) if len(avg_list) > 0 else 0
print(count)
print(float(avg_num))
