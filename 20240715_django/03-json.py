import json

list = ['Tom','Rose','Frank']

dict = {
    'id':1,
    'username':'Frank',
    'age':23,
    'sex':True
}

# 将PYTHON列表转换为JSON字符串

str1 = json.dumps(list)

# 将PYTHON字典转换为JSON字符串

str2 = json.dumps(dict)

print(str1)
print(str2)

#########################################################


str3 = '["Tom", "Rose", "Frank"]'
str4 = '{"id": 1, "username": "Frank", "age": 23, "sex": true}'

list1 = json.loads(str3)

dict1 = json.loads(str4)

print(list1)
print(dict1)





