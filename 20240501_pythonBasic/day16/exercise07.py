"""

"""


# list1 = [1, 10, 5, 2]
# 假设： 第一个值就是最大值
# maxv = list1[0]
# for i in range(1, len(list1)):
#     if maxv < list1[i]:
#         maxv = list1[i]
# print(maxv)


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


# 求这些人里面最高薪资的员工信息
# maxv = list_employees[0]
# for i in range(1,len(list_employees)):
#     if maxv.money < list_employees[i].money:
#         maxv = list_employees[i].money

def get_max(condition):
    print(condition)
    maxv = list_employees[0]
    for i in range(1, len(list_employees)):
        if condition(maxv) < condition(list_employees[i]):
            maxv = list_employees[i]
    return maxv


print(get_max(lambda item: item.money))


# 求这些人里面薪资的总和 年龄 成本 工龄...
# def sumv():
#     total = 0
#     for item in list_employees:
#         total += item.money
#     return total
#
#
# def condition01(item):
#     return item.money


def sum_value(condition):
    total = 0
    for item in list_employees:
        total += condition(item)
    return total

print(sum_value(lambda item: item.money))
print(sum_value(lambda item: item.eid))
print(sum_value(lambda item: item.did))
