from datetime import date


def get_weekday(year, month, day):
    """
    根据输入的年月日，输出该日期是星期几
    :param year:
    :param month:
    :param day:
    :return:
    """
    weekday = date(year, month, day).weekday()
    weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return weekdays[weekday]


weekday_1 = get_weekday(2024, 6, 17)
print(weekday_1)
