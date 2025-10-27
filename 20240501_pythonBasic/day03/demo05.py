"""
for循环
"""
# range(开始，结束，间隔) 产生指定范围内的整数
# for i in range():
#     循环体 语句组

# 不包含结束值 range(开始，结束，间隔)
for item in range(1,5,1):
    print(item)

print("--------------------------------")

# 间隔默认为1 range(开始，结束)
for item in range(1,5):
    print(item)

print("--------------------------------")

# 默认从0开始 range(结束)
for item in range(5):
    print(item)

