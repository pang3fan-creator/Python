"""
定义一个函数， 根据输入的年月日， 计算生活了多少天
例如： 2010 1 1  5281天
"""
from datetime import datetime


def calc_days(year, month, day):
    """
    根据生日计算活了多少天
    :param year: int 出生年
    :param month: int 出生月
    :param day: int 出生日
    :return: int 天数
    """
    date = datetime(year, month, day)
    times = datetime.now() - date

    return times.days


print(calc_days(2010, 1, 1))
