from datetime import datetime, date, timedelta


def get_weekday(year, month, day):
    d_1 = date(year, month, day)
    weekday_1 = d_1.weekday()
    list_weekday = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return list_weekday[weekday_1]


if __name__ == '__main__':
    a = get_weekday(2024, 6, 17)
    print(a)
