"""

"""


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return f"员工编号{self.eid}姓名是{self.name}部门为{self.did}薪资是{self.money}"


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

emp1 = max(list_employees, key=lambda emp: emp.money)
emp2 = min(list_employees, key=lambda emp: emp.money)
print(emp1)
print(emp2)

# 查部门是9002的员工 过滤器
for item in filter(lambda item: item.did == 9002, list_employees):
    print(item)

# 查看所有员工的姓名
for item in map(lambda item: item.name, list_employees):
    print(item)
