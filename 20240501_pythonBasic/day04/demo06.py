"""
深浅拷贝
避免数据意外修改  保存数据的原始快照，方便对比或者回滚

"""
list_movie = ["八角笼中", ["消失的她", "钢铁侠"]]

# 1. 赋值 数据1份 互相影响
# list_new = list_movie
# list_new[0] = "满江红"
# print(list_new)  # ['满江红', ['消失的她', '钢铁侠']]
# print(list_movie)  # ['满江红', ['消失的她', '钢铁侠']]

# 由于list_new是列表，所以可使用索引方式取值
# 又由于取到的值还是列表，所以可以继续使用索引方式取值
# print(list_new[1][0])
# list_new[1][0] = "碟中谍"
# print(list_new) # ['满江红', ['碟中谍', '钢铁侠']]
# print(list_movie) # ['满江红', ['碟中谍', '钢铁侠']]

# 2. 先切片再赋值
# 浅拷贝  第一层数据2份(互不影响)，深层数据1份(互相影响)
# 复制第一次数据，共享深层的数据
# list_new = list_movie[:]
# print(list_movie)
# print(list_new)

# list_new[0] = "满江红"  # ['满江红', ['碟中谍', '钢铁侠']]
# list_new[1][0] = "碟中谍"  # ['八角笼中', ['碟中谍', '钢铁侠']]
# print(list_new)
# print(list_movie)

# 3. 深拷贝 数据2份，互不影响
# 复制所有层的数据，拷贝后的数据完全独立
import copy

list_new = copy.deepcopy(list_movie)
print(list_movie)
print(list_new)

list_new[0] = "满江红"  # ['满江红', ['碟中谍', '钢铁侠']]
list_new[1][0] = "碟中谍"  # ['八角笼中', ['消失的她', '钢铁侠']]
print(list_new)
print(list_movie)
