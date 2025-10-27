"""
容器类型：列表
由一系列变量组成的可变序列容器
"""
list_moive = ["八角笼中", "封神第1部", "消失的她"]
print(list_moive)

# 获取 [索引] 从0开始
# 列表的最大长度 - 1 = 最大索引
print(list_moive[1])
# 修改或替换列表元素
list_moive[1] = "封神第三部"

# 超出范围 报错
# print(list_moive[10])
# list_moive[8] = "封神第8部"

# 新增
list_moive.append("蜘蛛侠")
list_moive.insert(1,"绿巨人")
print(list_moive)


