"""
内置的高阶函数
"""
list1 = [62, 1, 9, 4, 52, 21]

# 排序 从小到大
print(sorted(list1))

# 排序 从大到小
print(sorted(list1, reverse=True))


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
# 薪资排序 从小到大
new_list1 = sorted(list_employees, key=lambda item: item.money)

# 薪资排序 从大到小
new_list2 = sorted(list_employees, key=lambda item: item.money, reverse=True)

