class EmployeeModel:
    def __init__(self, name, post, salary: float):
        self.name = name
        self.post = post
        self.salary = salary

    def __str__(self):
        return "姓名：%s，岗位：%s，工资：%s" % (self.name, self.post, self.salary)

    def __eq__(self, other):
        return self.name == other
