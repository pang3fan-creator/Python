"""
在终端中输入月份，打印对应的天数
1 3 5 7 8 10 12 31天
4 6 9 11 30天
2月 29天
如果超出月份则提示月份错误
"""
month = int(input("请输入月份："))

if 1 <= month <= 12:
    if month == 2:
        print("29天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30天")
    else:
        print("31天")
else:
    print("月份错误")
