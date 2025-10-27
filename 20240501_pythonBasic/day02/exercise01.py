"""
用户可以在终端中输入自己的姓名，
程序输出： 你好  xxx 欢迎来到Python世界
"""
name1 = input("请输入您的姓名：")
print("你好" + name1 + "欢迎来到Python世界")

usd = float(input("请输入美元："))
cny = usd * 7.233
print("%.2f美元等于%.2f人民币" % (usd, cny))
print(f"{usd} 美元等于{cny}")