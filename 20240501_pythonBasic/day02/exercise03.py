"""
在终端中输入确诊人数及治愈人数，输出治愈比例
"""
# 1. 获取数据
number_of_confirmed = int(input("请输入确诊人数："))
number_of_cured = int(input("请输入治愈人数："))

# 2. 逻辑计算  治愈人数 / 确诊人数 * 100
cure_ratio = number_of_cured / number_of_confirmed * 100

# 3. 输出
print("治愈比例：" + str(cure_ratio) + "%")

# --------------------------------------------------------

bool1 = True
bool2 = False
print(bool1, type(bool1), bool2, type(bool2))

b1 = bool(0)  # f
b2 = bool(0.0)  # f
b3 = bool(1.2)  # t  只要不是0 就是true
b4 = bool(-9)  # t
b5 = bool(None)  # f
b6 = bool(int(0.1))  # f
print(b1, b2, b3, b4, b5, b6)

b7=bool("")
print(b7,type(b7))
b8=bool("0")
print(b8,type(b8))
