"""
古代的秤 一斤16两 在终端中获取两， 计算是几斤几两
假设： 20两   ==> 1斤4两
"""
# 1.获取数据
total = int(input("请输入两数："))

# 2.逻辑计算
jin = total // 16
liang = total % 16

# 3.输出结果
# print("结果是：" + str(jin) + "斤" + str(liang) + "两")

# 格式化输出 f
print(f"结果是:{jin}斤{liang}两")

