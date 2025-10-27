"""
装饰器
  在不修改代码的同时，增强函数或者类的行为
  接收一个函数作为参数， 返回新的函数
  缺点： 语法复杂

语法：
  def 函数装饰器名称(func):
     def wrapper(参数 *args,**kwargs)
        需要添加的新功能
        res = func(*args,**kwargs)
        return res
    return wrapper

  @ 函数装饰器名称
  def 原函数名称(参数):
     函数体

  原函数(参数)
"""


# 装饰器函数
def new_func(func):
    def wrapper():
        func()
        print("新功能")

    return wrapper


# 原函数
# 等同于创建了一个和原函数名称相同的变量，关联内嵌函数，调用时执行内嵌函数
@new_func
def func1():
    print("旧功能1")

func1()
