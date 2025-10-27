"""
将2个列表合并成一个字典
"""
list_stu = ["老赵", "老刘", "老王"]
list_age = [25, 28, 30]

dict_new = {}

# zip object
# print(zip(list_stu, list_age))
for key, value in zip(list_stu, list_age):
    dict_new[key] = value
print(dict_new)

dict_new = {key: value for key, value in zip(list_stu, list_age)}
print(dict_new)

print(dict(zip(list_stu, list_age)))


