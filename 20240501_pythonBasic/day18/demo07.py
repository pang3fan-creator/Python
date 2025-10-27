"""
文件管理
文件读写
读  读取文件 从文件获取内容
    py  txt  自动解码

对象名 = open(路径,"操作模式",encoding="编码方式")
写  修改文件 修改文件的内容

"""
from pathlib import Path
from datetime import datetime

# 1. 打开文件
# name 名字
# mode 模式 默认r
#  r   只读   文件不存在报错
#  w   只写   文件不存在创建
#  r+  读写   文件不存在报错
#  w+  写读   文件不存在创建
#  a   追加   文件不存在创建
#  a+  追加读 文件不存在创建

# encoding 编码 Linux 默认UTF-8  Windows 默认gbk

# file = open("demo01.py")
# print(file)
# # 2. 读取
# print(file.read())
# # 3. 关闭
# file.close()

file = open("demo01.py", "r", encoding="utf-8")
try:
    # 2. 读取
    print(file.read())
finally:
    # 3. 关闭
    file.close()

# 简化try...finally
# 当with代码块全部执行完成后，无论是否有异常，都会自动释放资源
with open("demo01.py", "r", encoding="utf-8") as file:
    # print(file.read())
    print(file.read(5))  # 按照字符个数读取
    print(file.readlines())  # 把每行内容存到列表

# 离开缩进区域，自动调用close方法
