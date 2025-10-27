"""
闰年的计算  4位年份
如果能够被4整除但是不能被100整除，是闰年
如果可以被400整除，是闰年
终端中输入一个4位年份， 输出true或者false
"""
year = int(input("请输入4位数年份："))

bool1 = (year % 4 == 0)
bool2 = year % 100 != 0
bool3 = year % 400 == 0

print((bool1 and bool2) or bool3)
