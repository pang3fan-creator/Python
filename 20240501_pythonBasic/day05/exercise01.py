"""
    练习：生成10-30之间能够被3或者被5整除的数字
    [10,12,15,18,20,21,24,25,27,30]
"""
# 列表推导式
list_new = [item for item in range(10, 31) if item % 3 == 0 or item % 5 == 0]
print(list_new)
