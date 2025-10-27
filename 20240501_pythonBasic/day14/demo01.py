"""
模块 Module  一系列包含数据、函数、类的py文件
引入：
    import 模块名
    import 模块名 as 别名
使用：
    模块名.成员

原理：创建变量记录文件的地址，使用时通过变量名中的文件地址访问文件print(type(random))
中的成员

将模块整体导入到当前模块中

适用性：面向过程编程
"""
# 系统模块 python中内置的，不需要下载就可以直接使用
import random
import random as rd


print(random.randint(0, 10))
print(rd.randint(0, 10))

# print(type(random))  # module
# random = 10
# print(type(random))  # int 发生了重新赋值
