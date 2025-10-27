"""
1. 创建文件，module02.py
        文件中 拥有一个变量 data = 10086
       文件中 拥有一个say方法用来打招呼
       文件中 拥有一个MyClass类， 类中存在Hi方法用来打招呼
2. 在当前的文件中 打印变量 使用say方法  使用类的Hi方法
"""
import module02

print(module02.data)
module02.say()
module02.MyClass().hi()

from module02 import *

print(data)
say()
MyClass().hi()
