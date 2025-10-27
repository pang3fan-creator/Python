"""
创建字典，使用迭代思想，打印每个键值对，不需要自己实现
"""

dict1 = {
    "name": "huai ren",
    "age": 18,
    "sex": "男"
}
iterator = dict1.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict1[key])
    except StopIteration:
        break
