"""
使用生成器表达式在列表中获取所有的字符串
list1 = [43, "a", 5, True, 6, 7, 89, 9, "b"]

使用生成器表达式从列表中获取所有的整数， 并计算这些整数的平方
list2 = [1,2.3,5,6.2,7]

"""

list1 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
str_generator1 = (item for item in list1 if isinstance(item, str))
str_generator2 = (item for item in list1 if type(item) == str)
print(list(str_generator1))
print(list(str_generator2))

list2 = [1, 2.3, 5, 6.2, 7, 2.0]
str_generator3 = (item ** 2 for item in list2 if isinstance(item, int))
str_generator4 = (item ** 2 for item in list2 if type(item) == int)
print(list(str_generator3))
print(list(str_generator4))
