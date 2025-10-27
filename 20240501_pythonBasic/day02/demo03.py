"""
布尔值  真true 1  假false 0 注意大小写
"""
bool1 = True
bool2 = False
print(bool1, bool2)

# 转bool
b1 = bool(0)  # f
b2 = bool(0.0)  # f
b3 = bool(1.2)  # t  只要不是0 就是true
b4 = bool(-9)  # t
b5 = bool(None)  # f
b6 = bool(int(0.1))  # f
print(b1, b2, b3, b4, b5, b6)
