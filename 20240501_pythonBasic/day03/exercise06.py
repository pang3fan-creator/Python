"""
一张纸0.01毫米  珠峰 8844.43米
一张纸对折多少次后可以超过珠峰
请打印对折的次数及对折的厚度和对折的总次数

"""
# thickness = 0.00001
thickness = 1e-5  # 科学计数法
count = 0
while thickness < 8844.43:
    thickness *= 2
    count += 1
    print(f"{count}次对折后的厚度是：{thickness}")

print(f"一共对折{count}次")
