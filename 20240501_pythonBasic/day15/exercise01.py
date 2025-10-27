"""
封装一个函数记录整数成绩，
如果格式不正确，提示重新输入，反之输出成绩
"""


def score():
    try:
        numbers = int(input("请输入成绩："))
        print(f"您的成绩是：{numbers}")
    except:
        print("格式不正确，重新输入")

score()
