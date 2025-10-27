"""
汇率转换器   美元 人民币  1美元 * 7.233 = 人民币
数据类型： str字符串 小数float 整数int
检查数据类型的函数： type()
逆天改命： 使用函数强制修改数据的数据类型
float() 转化成小数
str() 转化成字符串
int() 转化成整数
结果 = 目标类型(待转数据)
"""
# 1. 获取数据：美元
# float() 内置函数
usd = float(input("请输入美元："))
# print(type(usd)) # str

# 2. 逻辑计算 美元 * 7.233
cny = usd * 7.233

# 3. 显示结果 xx美元 = xx人民币
print(str(usd)+ "美元 = " + str(cny) + "人民币")
