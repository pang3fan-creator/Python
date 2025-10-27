"""
字典推导式
语法： 字典 = {键:值 for 变量 in 可迭代对象}
"""
# 2个列表合并成为一个字典
list_name = ["八角笼中","封神第一部","消失的她"]
list_pop = [12321,45667,96876]

dict_movie = {
    list_name[i]:list_pop[i] for i in range(len(list_name))
}
print(dict_movie)