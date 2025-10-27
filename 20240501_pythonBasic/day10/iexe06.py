class Student:
    """
    学生类
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = {}

    def add_score(self, subject, score):
        if 0 <= score <= 100:
            self.scores[subject] = score
        else:
            print("输入有误，请重新输入")

    def get_avg(self):
        try:
            average_score = sum(self.scores.values()) / len(self.scores)
        except ZeroDivisionError:
            return 0
        except:
            print("未知错误")
        else:
            return average_score


stu_zs = Student("法外狂徒张三", 20)
stu_zs.add_score("语文", 90)
stu_zs.add_score("数学", 85)
stu_zs.add_score("英语", 95)
print(stu_zs.scores)
print(stu_zs.get_avg())
