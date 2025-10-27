"""
温度转换器：
    摄氏度 = （华氏度 - 32） 除以 1.8
    华氏度 = 摄氏度 * 1.8 + 32
    在终端中录入摄氏度，计算华氏度
"""
# 1.获取数据
centigrade_degree = float(input("请输入摄氏度："))

# 2.逻辑计算
fahrenheit_degree = centigrade_degree * 1.8 + 32

# 3.输出
print(f"华氏度：{fahrenheit_degree}")
