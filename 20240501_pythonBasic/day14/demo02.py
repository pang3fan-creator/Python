"""
自己写的模块 然后 自己调用
其实引入的模块名就是py文件的文件名

第二种导入方法：
    from 模块名 import 成员名
    from 模块名 import 成员名 as 别名
    from 模块名 import *
将模块内的成员导入到当前模块的作用域
使用：
   直接使用成员名

适用性：面向对象
"""
# 引入自己的自定义模块
import module01

module01.fun1()
module01.fun2()

# 如果我只想要引入其中的某一个成员
from module01 import fun1

fun1()

# 全部引入
from module01 import *

fun1()
fun2()

# 给引入的某个成员起别名
from module01 import fun2 as f2
def fun2():
    print("fun2 我是珍妮弗")
fun2()
f2()
