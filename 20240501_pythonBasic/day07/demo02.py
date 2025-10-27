"""
函数内存图
"""


# 1. 将函数加载到内存的代码区
def add(m, n):
    data = m + n
    return data


num = 2
# 2. 调用函数时，会开辟空间(栈帧)存储在函数内部创建的变量
res = add(1, num)

# 3.函数执行后，该空间立即释放
print(res)
