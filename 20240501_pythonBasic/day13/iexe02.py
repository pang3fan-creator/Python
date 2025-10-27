class Employee:
    def __init__(self, name, age, salary, post):
        self.name = name
        self.age = age
        self.salary = salary
        self.post = post

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


employee_1 = Employee("Ivan", 25, 2000, "engineer")
employee_2 = Employee("Ivan", 25, 2000, "engineer")
print(employee_1 == employee_2)
employee_3 = Employee("Ivan_1", 25, 20000, "engineer")
employee_4 = Employee("Ivan_1", 25, 2000, "engineer")
print(employee_3 == employee_4)
