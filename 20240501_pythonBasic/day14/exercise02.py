"""
定义一个函数， 根据输入的年月日， 计算那天是星期几
2024 6 17 星期一
"""
from datetime import datetime


def calc_weekday(year, month, day):
    """
    根据输入的年月日，计算星期几
    :param year: int 年份
    :param month: int 月份
    :param day: int 日
    :return: str 星期名称 星期一
    """
    date = datetime(year, month, day)
    week_index = date.weekday()

    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    return week_list[week_index]


# print(f"星期{calc_weekday(2024, 6, 16) + 1}")
print(calc_weekday(2024, 6, 16))
