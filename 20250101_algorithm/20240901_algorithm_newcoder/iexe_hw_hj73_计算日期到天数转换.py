"""
根据输入的日期，计算是这一年的第几天。
保证年份为4位数且日期合法。
"""
from datetime import datetime

while True:
    try:
        year, month, day = input().strip().split(' ')
        date_obj = datetime.strptime(year + '-' + month + '-' + day, '%Y-%m-%d')
        date_obj_start = datetime.strptime(year + '-01-01', '%Y-%m-%d')
        print(int((date_obj - date_obj_start).days) + 1)
    except:
        break
