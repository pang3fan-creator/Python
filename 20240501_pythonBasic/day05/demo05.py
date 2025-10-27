"""
创建字典存储台湾的 地区、新增、现有 感染人数
创建字典存储北京的 地区、新增、现有 感染人数

给 台湾和北京 添加累计确诊人数 和 治愈人数

给 台湾和北京 的累计确诊人数 和 治愈人数 各自增加10

删除台湾和北京的新增信息

打印 台湾和北京 2个字典的所有的值
"""
dict_1 = {
    "region": "台湾",
    "new": 1552,
    "now": 262
}

dict_2 = {
    "region": "北京",
    "new": 545,
    "now": 23
}

dict_1["total"] = 4559
dict_2["total"] = 633

dict_1["cure"] = 1
dict_2["cure"] = 2

# 修改
dict_1["total"] += 10
dict_2["total"] += 10

dict_1["cure"] += 10
dict_2["cure"] += 10

# 删除
del dict_1["new"]
del dict_2["new"]

# 遍历
for value in dict_1.values():
    print(value)

for key, value in dict_2.items():
    print(value)

print(dict_1)
print(dict_2)
