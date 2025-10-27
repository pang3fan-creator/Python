"""
切片 定位多个元素
"""
list_moive = ["八角笼中", "封神第1部", "消失的她", "蜘蛛侠", "绿巨人", "钢铁侠"]
# 容器名[开始:结束:间隔]
# 包含开始内容， 不包含结束内容
# 正数： 从左到右   负数：从右到左
# print(list_moive[1:5:1])
# print(list_moive[0:5:2])
# print(list_moive[-5:5:2])
# print(list_moive[-5:-1:2])
# print(list_moive[-1:-5:-2])

# 容器名[开始:结束] 间隔默认为1
print(list_moive[1:5])
# 容器名[索引]
print(list_moive[5],type(list_moive[5]))
# 容器名[:结束]  开始默认为0
print(list_moive[:2])  # ['八角笼中', '封神第1部']

# 容器名[开始:]  结束默认到结尾
print(list_moive[3:])  # ['蜘蛛侠', '绿巨人', '钢铁侠']
print(list_moive[-3:])  # ['蜘蛛侠', '绿巨人', '钢铁侠']

# 容器名[开始::] 结束默认到结尾 默认间隔
print(list_moive[-3::])  # ['蜘蛛侠', '绿巨人', '钢铁侠']
# 容器名[::间隔]  默认开始  默认结尾
print(list_moive[::2])  # ['八角笼中', '消失的她', '绿巨人']
