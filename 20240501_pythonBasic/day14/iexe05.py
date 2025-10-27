from datetime import date


def get_age(year, month, day):
    """
    根据输入的年月日，计算总共活了多少天
    :param year:
    :param month:
    :param day:
    :return:
    """
    today = date.today()
    birthday = date(year, month, day)
    print(type(today - birthday))
    return (today - birthday).days


age_1 = get_age(1999, 9, 11)
print(age_1)


def get_zodiac(year):
    """
    根据输入的年月日，计算生肖
    :param year:
    :return:
    """
    zodiac_list = ['猴', '鸡', '狗', '猪', '鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊']
    return zodiac_list[year % 12]


print(get_zodiac(1991))
print(get_zodiac(1992))
print(get_zodiac(1983))
