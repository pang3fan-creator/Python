"""
颠倒字典的键和值
"""
dict_info = {
    "1001": "北京",
    "1002": "天津",
    "1003": "杭州",
    "1004": "深圳"
}
dict_new = {}

for key, value in dict_info.items():
    dict_new[value] = key

print(dict_new)

dict_new1 = {value: key for key, value in dict_info.items()}
print(dict_new1)