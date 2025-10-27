class EmpModel:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return f'编号：{self.eid} 部门：{self.did} 名字：{self.name} 工资：{self.money}'


list_emps = [EmpModel(1001, 9002, "师父", 60000),
             EmpModel(1002, 9001, "孙悟空", 50000),
             EmpModel(1003, 9002, "猪八戒", 20000),
             EmpModel(1004, 9001, "沙僧", 30000),
             EmpModel(1005, 9001, "小白龙", 15000)]

# 求这些人里薪资最高的员工信息

aaa = max(list_emps, key=lambda item: item.money)
print(aaa)


def function_1(func):
    temp = list_emps[0]
    for item in list_emps:
        if func(temp, item):
            temp = item
    return temp


find_1 = function_1(lambda temp, item: temp.money < item.money)
print(find_1)
find_2 = function_1(lambda temp, item: temp.money > item.money)
print(find_2)


def function_2():
    temp = [item.money for item in list_emps]
    return sum(temp)


find = function_2()
print(find)
