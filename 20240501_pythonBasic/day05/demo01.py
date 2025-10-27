"""
字符串 有一系列编码值组成的不可变序列容器

格式化字符串
     将变量按照某种固定的格式呈现
     语法： 格式 % (变量)
     占位符： 原样%s  保留小数精度%.2f 保留位数%.2d
     如果是打印% 则需要 %% 格式
"""
print("万岁")
print('万岁')
print("""'万岁'""")

# 转义符 改变某些含义的特殊符号
# \ 反斜线/杠 \n 换行符  如果想要输出字符\ 则需要使用\\
print("北京海淀区\"万寿路\"18号院")
print("北京海淀区\n万寿路\n18号院")
print("北京海淀区\\n万寿路\\18号院")

usd = float(input("请输入美元："))
cny = usd * 7.233
print(str(usd) + "美元 = " + str(cny) + "人民币")
print("%s美元 = %s人民币" % (usd, cny))
print("%s美元 = %.2f人民币" % (usd, cny))

minute = 1
second = 2
print("%.3d:%.2d" % (minute, second))

number = 99
print("马上要签到，不能低于%s%%" % (number))

