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


def find_emps(function):
    for model in list_emps:
        if function(model):
            yield model


find_1 = find_emps(lambda model: model.did == 9001)
for item in find_1:
    print(item)
print()
find_2 = find_emps(lambda model: len(model.name) == 2)
for item in find_2:
    print(item)
