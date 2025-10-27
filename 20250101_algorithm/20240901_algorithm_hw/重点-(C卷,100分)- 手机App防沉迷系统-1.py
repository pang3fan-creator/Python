class App:
    def __init__(self, name, priority, start, end):
        self.name = name
        self.priority = priority
        self.start = start
        self.end = end


def convert(time):
    # 时间格式 HH:MM，小时和分钟都是两位，不足两位前面补0
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


# 算法入口
def getResult():
    registereds = []

    for app in apps:
        # 起始时间>=结束时间，则注册不上
        if app.start >= app.end:
            continue

        # 记录已注册的App中被注销的App的位置
        idxs = []

        flag = False

        # 比较app_registering和它前面完成注册的所有app_registered
        for j in range(len(registereds)):
            registered = registereds[j]

            # 两个App的注册时间无冲突，则继续和下一个app_registered比较
            if registered.start >= app.end or app.start >= registered.end:
                continue

            # 两个App的注册时间有冲突，则比较优先级
            if app.priority > registered.priority:
                # 这里不能直接注销低优先级的app_registered，我们要保证app_registering一定能注册后才能进行此操作，因此先记录要被注销的app_registered的位置
                idxs.append(j)
            else:
                # app_registering的优先级 <= app_registered的优先级时，则app_registering不能注册，终止比较
                flag = True
                break

        # 如果app_registering不能注册，则终止比较
        if flag:
            continue

        # idxs中索引是升序的，如果正序删除的话，那么每删除一个元素，都会改变后面元素的索引位置，因此这里采用倒序删除
        idxs.reverse()
        for idx in idxs:
            registereds.pop(idx)

        registereds.append(app)

    ans = "NA"

    # 注册成功的App时段之间互不冲突，因此queryTime只会对应一个App
    for registered in registereds:
        if registered.start <= queryTime < registered.end:
            ans = registered.name
            break

    return ans


if __name__ == '__main__':
    # 输入获取
    n = int(input())

    # 需要注册的App
    apps = []
    for _ in range(n):
        name, priority, start, end = input().split(" ")
        apps.append(App(name, int(priority), convert(start), convert(end)))

    # 需要查询的时间点
    queryTime = convert(input())

    # 算法调用
    print(getResult())
