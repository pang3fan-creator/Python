"""
测智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
终端中输入心里年龄和实际年龄 输出智商等级
天才： 140及以上
超常： 120 ~ 139
聪慧： 110 ~ 119
正常： 90 ~ 109
"""
ma = int(input("请输入心理年龄："))
ca = int(input("请输入实际年龄："))
iq = ma / ca * 100

if iq >= 140:
    print("天才")
elif 120 <= iq < 140:
    print("超常")
elif 110 <= iq < 120:
    print("聪慧")
elif 90 <= iq < 110:
    print("正常")

# 只判断单边（需要注意顺序！）
if iq >= 140:
    print("天才")
elif iq >= 120:
    print("超常")
elif iq >= 110:
    print("聪慧")
elif iq >= 90:
    print("正常")
else:
    print("低级")
