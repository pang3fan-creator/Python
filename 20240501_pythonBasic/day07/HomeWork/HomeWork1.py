"""
   定义函数,根据年龄，计算对应的人生阶段
    age = int(input("请输入年龄："))
    if age <= 6:
        print("童年")
    elif age <= 17:  # 程序能执行到本行,说明age一定大于6
        print("少年")
    elif age <= 40:
        print("青年")
    elif age <= 65:
        print("中年")
    else:
        print("老年")
"""
import sys


def calc_life(age):
    # if age <= 6:
    #     print("童年")
    # elif age <= 17:  # 程序能执行到本行,说明age一定大于6
    #     print("少年")
    # elif age <= 40:
    #     print("青年")
    # elif age <= 65:
    #     print("中年")
    # else:
    #     print("老年")

    # 返回值：函数定义者告诉函数调用者的结果 return 数据
    if age <= 6:
        return "童年"
    elif age <= 17:
        return "少年"
    elif age <= 40:
        return "青年"
    elif age <= 65:
        return "中年"
    else:
        return "老年"


age = int(input("请输入年龄："))

print(calc_life(age))
life = calc_life(age)
print(life)

print(f"这里是一群{calc_life(age)}人在踢球")
