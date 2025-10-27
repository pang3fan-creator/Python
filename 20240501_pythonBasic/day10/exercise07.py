"""
创建一个学生类 三个属性(init参数传递时只需要传2个)
    姓名 name 年龄 age 成绩 scores 用字典表示
add_score(subject,score) 添加一个科目的成绩
get_avg() 计算并返回成绩平均分
使用实例：
stu = Student("张三",20)
stu.add_score("cn",100)
stu.get_avg() # 100分
"""


class Student:
    # def __init__(self,name,age,scores={}):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = {}

    def add_score(self, subject, score):
        if score >= 0 and score <= 150:
            self.scores[subject] = score
        else:
            print("请输入正确范围的成绩")

    def get_avg(self):
        # 如果没有成绩信息(空字典)，意味着判断时是false， 直接返回0
        # if self.scores:
        #     # 字典求和 求平均值
        #     total = 0  # 记录总成绩
        #     count = 0  # 记录循环次数，因为循环次数等于学科数量
        #     for item in self.scores.values():
        #         total += item
        #         count += 1
        #
        #     return total / count
        # else:
        #     return 0

        # 第二种
        # if self.scores:
        #     # 字典求和 求平均值
        #     return sum(self.scores.values()) / len(self.scores)
        # else:
        #     return 0

        # 第三种
        if not self.scores:
            return 0
        # 字典求和 求平均值  {"cn":0,"en":0}
        return sum(self.scores.values()) / len(self.scores)

stu = Student("张三", 20)
stu.add_score("cn", 100)
stu.add_score("en", 20)
print(stu.get_avg())

stu2 = Student("李四", 20)
stu2.add_score("cn", 0)
stu2.add_score("en", 0)
print(stu2.get_avg())
