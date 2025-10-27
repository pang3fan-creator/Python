"""
封装一个函数，传递苹果的个数，计算每个人能分到多少苹果
函数中通过input来输入人数

异常处理， 可以将程序有异常转化为正常流程
except 子句可以有1个或者多个，用来捕获某种类型的错误
finally 子句可有可无，做多只能有1个，如果没有except子句，finally必须存在
"""


# 对症下药 无论代码中是否发生异常，都会执行finally的代码
def apple(count):
    try:
        person = int(input("请输入人数："))
        res = count / person
        print(f"每个人可以分的{res}个苹果")
        # ZeroDivisionError
        # ValueError
    except ZeroDivisionError:
        print("不能输入零！")
    except ValueError:
        print("只能输入正整数！")
    finally:
        print("分苹果结束")


apple(10)
