"""
创建员工类 姓名 岗位 年龄 薪资
比较某2位员工的薪资是否一样，如果薪资一样则返回true
比较某2位员工信息是否全都一致，如果一致返回true


"""


class Dep:
    def __init__(self, name, job, age, salary):
        self.name = name
        self.job = job
        self.age = age
        self.salary = salary

    def __eq__(self, other):
        # return self.salary == other.salary
        return self.__dict__ == other.__dict__
        # return self.salary == other.salary, \
        #        self.name == other.name, \
        #        self.job == other.job,\
        #        self.age == other.age


d1 = Dep("laozhao", "web", 18, 18)
d2 = Dep("laozhao", "web", 18, 18)

print(d1 == d2)
