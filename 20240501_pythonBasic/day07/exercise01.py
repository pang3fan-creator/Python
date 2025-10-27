"""
使用函数完成
古代的秤 一斤16两 在终端中获取两， 计算是几斤几两
假设： 20两   ==> 1斤4两
从表面上看， return可以返回多个值 值与值之间使用英文逗号分割
但实际上是return 返回的是一个元组(实际接收)
元组的特殊写法：
    元组名 =  "八角笼中","封神"
    元组名 =  "八角笼中",
    元组名 =  1,2
"""


def calc_weight(total):
    jin = total // 16
    liang = total % 16

    return jin, liang


total = int(input("请输入两数："))
res = calc_weight(total)
print(res)  # (1, 4)
print(f"结果是:{res[0]}斤{res[1]}两")
