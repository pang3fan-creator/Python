"""
异常处理， 真实的处理了预知的异常
"""
# try尝试运行这一段代码，如果没问题就正常执行逻辑
# 如果有问题则执行except的语句
try:
    number = int(input("请输入人数："))
    print(f"一共有{number}人，需要{number * 2}个苹果")
except:
    print("请输入数字")

try:
    number = int(input("请输入年龄，大于18："))
except:
    # 错误处理， 只要是try中的代码报错，我就把number变为18
    number = 18

print(f"您的年龄是{number}，可以访问~")
