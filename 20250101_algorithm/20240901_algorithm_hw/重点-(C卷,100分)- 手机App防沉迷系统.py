def append_app(mobile_app):
    for i, item in enumerate(list_app):
        if item.time1 >= mobile_app.time2 or item.time2 <= mobile_app.time1:
            continue
        else:
            if mobile_app.authority > item.authority:
                list_app[i] = mobile_app
            return
    list_app.append(mobile_app)


class MobileApp(object):
    def __init__(self, name, authority, time1, time2):
        self.name = name
        self.authority = authority
        self.time1 = self.time_convert(time1)
        self.time2 = self.time_convert(time2)

    @staticmethod
    def time_convert(time1):
        hour, minute = map(int, time1.split(':'))
        return int(hour) * 60 + int(minute)


if __name__ == '__main__':
    N = int(input())
    list_app = []
    for _ in range(N):
        name, authority, time1, time2 = input().split(' ')
        mobile_app = MobileApp(name, authority, time1, time2)
        append_app(mobile_app)
    time_use = MobileApp.time_convert(input())
    for app in list_app:
        if app.time1 <= time_use <= app.time2:
            print(app.name)
            exit()
    print('NA')
