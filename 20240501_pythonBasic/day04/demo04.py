"""
移除数据
"""
list_moive = ["八角笼中", "封神第1部", "消失的她", "蜘蛛侠", "钢铁侠"]
list_moive.remove("八角笼中")
print(list_moive)

# del 直接操作原数据
del list_moive[0]
del list_moive[:2]
print(list_moive)
