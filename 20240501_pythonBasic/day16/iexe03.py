list01 = [342, 4, 54, 56, 6776]


# 定义函数,在列表中查找第一个大于100的数
def get_number_gt_100():
    for number in list01:
        if number > 100:
            return number


# 定义函数,在列表中查找第一个偶数
def get_number_by_even():
    for number in list01:
        if number % 2 == 0:
            return number


# 参数：得到的是列表中的元素
# 返回值：对列表元素判断后的结果(True False)
def condition01(number):
    return number > 100


def condition02(number):
    return number % 2 == 0


# 变化点函数：查找小于10的数据
def condition03(number):
    return number < 10


# 通用函数
def find_single(condition: callable,list_1: list):  # 抽象
    for item in list_1:
        if condition(item):  # 统一
            return item


print(find_single(condition02, list01))
