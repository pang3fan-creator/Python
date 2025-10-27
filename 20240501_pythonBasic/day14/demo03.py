"""
时间模块
"""
from datetime import datetime, timedelta

# 1. 表达时间
# 现在时间
d1 = datetime.now()
# 年月日
d2 = datetime(2000, 8, 8)
# 年月日 时分秒
d3 = datetime(2024, 6, 17, 15, 15, 15)
print(d1)
print(d2)
print(d3)
# print(d3.__str__) # datetime对象

# 2.计算时间
delta01 = d3 - d2
print(delta01)
print(delta01.total_seconds())
print(d3 + timedelta(weeks=1))
print(d3.replace(month=d3.month + 1))

# 3. 格式化时间日期
print(d3.strftime("%Y年%m月%d日 %H时%M分%S秒"))
print(d3.strptime("2000年11月01日 15时15分15秒", "%Y年%m月%d日 %H时%M分%S秒"))

# 4. 获取
print(d3.year)
print(d3.month)
print(d3.day)
print(d3.second)
print(d3.hour)
print(d3.minute)
print(d3.date())
# 返回的是周几的索引 周一是第一天索引为0
print(d3.weekday())
