"""
继承
 人      老师           学生
说话     say教学      say问问题
"""


class Peron:
    def say(self):
        print("说话")


class Teacher(Peron):
    def teach(self):
        self.say()
        print("讲课")


class Student(Peron):
    def study(self):
        self.say()
        print("问问题")


shenge = Teacher()
shenge.say()
shenge.teach()

stu = Student()
stu.say()
stu.study()
