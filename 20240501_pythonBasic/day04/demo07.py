"""
列表推导式 通过简单的语法把可迭代对象转化成新列表
简化代码
"""
# 需求：大于60的数添加到新列表中
list_number = [66, 25, 71, 86, 57]

# 传统写法
# list_new = []
# for item in list_number:
#     if item > 60:
#         list_new.append(item)

# 列表推导式
# 新列表 = [表达式 for 变量 in 可迭代对象]
# 新列表 = [表达式 for 变量 in 可迭代对象 if 条件]
# 表达式：针对于 可迭代对象的操作（计算）
# 变量： 每一个元素
# 可迭代对象：列表 元组等
# 如果有if 过滤元素
list_new = [item for item in list_number if item > 60]

print(list_new)
