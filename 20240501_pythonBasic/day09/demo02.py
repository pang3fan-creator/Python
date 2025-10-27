"""
代码内存图
"""
data01 = 10

def func01(p):
    global data01
    data01 += 1
    p += 1


data02 = 10
func01(data02)
func01(data02)
print(data01)  # ? 12
print(data02)  # ? 10
