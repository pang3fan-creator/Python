"""
面向对象
类 一系列变量和方法(函数) 组成的新的数据类型  抽象
对象 类的实例化后的结果 具体

跨类调用

mvc设计模式(架构) 分层3层 各司其职分工
M Model         模型层  数据模型的封装
V View          视图层  显示视图
C Controller    控制层  存储、计算

三大特性：封装 继承 多态
封装： 在类中隐藏实现的细节 借助私有属性和私有方法 __
继承：子承父业 子类(父类):
子类直接拥有父类的方法
子类没有构造函数时，自动执行父类的构造函数
子类有构造函数时，会覆盖父类的构造函数，super()函数调用父类的构造函数

"""
# 浮点数精度验证
a = 0.1
b = 0.7
print(8 == (a + b) * 10)  # False

a = 0.2
b = 0.6
print(8 == (a + b) * 10)  # True

# 容器类型验证
list1 = ["xiaoyi", "xiaoyu", "tongtong", "linlin", "qincai"]
tuple1 = ("xiaoyi", "xiaoyu", "tongtong", "linlin", "qincai")

list1[0] = "小艺"
print(list1)

# tuple1[0] = "小艺" #不可变 报错
print(tuple1[1:4])
print(tuple1[1:4:2])

list2 = []
tuple2 = ()
print(list2.__sizeof__())  # 40
list2.append(123)
print(list2.__sizeof__())  # 72
list2.append("hehe")
print(list2.__sizeof__())  # 72
print(list2)

print(tuple2.__sizeof__())  # 24

# 集合
set1 = {"怨种", 3, 123, 555, 22, 33}
# set1.add(66)
# set1.remove(2)
print(set1)
print(set1.pop())
print(set1)

# 常见方法
list3 = [2, 1, 1, 3]
list3.reverse()
print(list3)

list3.sort()
print(list3)

list3.reverse()
print(list3)

print(list3.count(1))
