"""
让代码重复的执行，
如果大于0 输出 正数
如果小于0 输出 负数
如果等于0 退出循环
"""
while True:
    number = int(input("请输入数字："))
    if number > 0:
        print("正数")
    elif number < 0:
        print("负数")
    elif number == 0:
        break

print("后续逻辑")