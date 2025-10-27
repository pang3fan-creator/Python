"""
内置装饰器@staticmethod
"""
class Stu:
    # 可以在不实例化类的情况下，直接访问该方法
    # 不需要约定默认参数self
    @staticmethod
    def say():
        print("青山不改，绿水长流")


# 实例化类 推荐
# Stu().say()
Stu.say()
