"""
写： 把内存中的对象写到文件里
读： 读取文件中的内容作为代码执行
"""


class StuModel:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 对象转字符串：给人看的 格式没有要求
    def __str__(self):
        return f"姓名是：{self.name},年龄：{self.age},性别：{self.sex}"

    # 对象转字符串: 给机器用的 格式要符合python的语法
    # 返回一个对象的“官方”字符串表示形式
    def __repr__(self):
        # return 'StuModel("%s","%s","%s")' % (self.name, self.age, self.sex)
        return f"StuModel('{self.name}','{self.age}','{self.sex}')"


s1 = StuModel('xiaoyi', "18", "女")
print(s1)

# 将内存中的对象写入到文件
with open("data.txt", "w", encoding="utf-8") as file:
    file.write(s1.__repr__())

# 将文件中的内容读取到内存，继续作为对象使用
with open("data.txt", "r", encoding="utf-8") as file:
    # 读取到的内容： StuModel("xiaoyi", "18", "女")
    # 意味着 对象.属性取值 eval()
    # s2 = file.read() #依然是字符串

    # eval() 把括号中的内容当做代码去执行
    s2 = eval(file.read())
    print(s2.name)
