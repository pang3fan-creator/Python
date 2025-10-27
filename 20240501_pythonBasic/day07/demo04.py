"""
画出函数内容存图
不可变数据
可变数据
"""

def func01(p1, p2):
    p1 = 20
    # 函数内部修改了传递的可变数据，不需要return返回结果
    # 函数外的可变数据依然会改变
    p2[0] = 20

data01 = 10
data02 = [10]

func01(data01, data02)

print(data01)
print(data02)
