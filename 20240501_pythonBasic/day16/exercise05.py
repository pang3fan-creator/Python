"""
定义生成器函数，在员工列表中查找所有部门是9001的员工
定义生成器函数，在员工列表中查找所有姓名是2个字的员工
使用lambda表达式重构
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


def find_all(condition):
    for item in list_employees:
        if condition(item):
            yield item

for item in find_all(lambda item: item.did == 9001):
    print(item)
for item in find_all(lambda item: len(item.name) == 2):
    print(item)
