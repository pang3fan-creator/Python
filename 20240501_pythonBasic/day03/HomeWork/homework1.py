"""
根据父母身高,预测儿子身高.
    步骤:获取父亲身高
        获取母亲身高
        显示儿子身高
    公式:(父亲身高+母亲身高)*0.54
"""
# 1.获取数据
father_h = float(input("请输入父亲的身高CM："))
mother_h = float(input("请输入母亲的身高CM："))

# 2.逻辑计算
son_h = (father_h + mother_h) * 0.54

# 3.输出
print(f"预测儿子的身高是：{son_h}厘米")

# a, b = 1, 2
# a, b = b, a
# print(a, b)
