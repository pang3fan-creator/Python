"""
定义生成器函数，在员工列表中查找所有部门是9001的员工
定义生成器函数，在员工列表中查找所有姓名是2个字的员工
步骤：
    -- 根据需求，写出函数。
    -- 因为主体逻辑相同,核心算法不同.
       所以使用函数式编程思想
       创建高阶函数find_all
   -- 在当前模块中调用
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


# 定义生成器函数，在员工列表中查找所有部门是9001的员工
def find_1():
    for item in list_employees:
        if item.did == 9001:
            yield item


# 定义生成器函数，在员工列表中查找所有姓名是2个字的员工
def find_2():
    for item in list_employees:
        if len(item.name) == 2:
            yield item


# for item in find_1():
# for item in find_2():
#     print(item)

def condition01(item):
    return item.did == 9001


def condition02(item):
    return len(item.name) == 2


def find_all(condition):
    for item in list_employees:
        if condition(item):
            yield item


for item in find_all(condition01):
    print(item)
for item in find_all(condition02):
    print(item)

