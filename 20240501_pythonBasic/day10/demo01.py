"""
类  ==>  变量 + 函数(方法)组成的新的数据类型
对象

"""
dict1 = {"name": "封神", "type": "动作"}
dict2 = {"name": "阿凡达", "type": "科幻"}

print(type(dict1))


# 事物共同的特点 ==> 类是一类事物的抽象  ==> 表头
class Movie:
    # 构造函数 创建对象时被调用 给对象赋值
    # self 创建的对象  约定俗称的
    def __init__(self, name, type_):
        # 对象.属性
        self.name = name
        self.type = type_


# 实例化类  对象  具体数据
# 对象名存储的是实例化后的对象的地址
m1 = Movie("封神", "动作")
m2 = Movie("阿凡达", "科幻")
# 获取属性值 ： 对象.属性
print(m1.name,type(m1))
print(m2.type,type(m2))


