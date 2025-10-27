list01 = [43.2, "a", 5, True, 6, 7, 89.9, 9, "b"]

# 使用生成器表达式在列表中获取所有字符串.
my_generator = ({i: item} for i, item in enumerate(list01) if isinstance(item, str))
for i in my_generator:
    print(i)

# 在列表中获取所有整数,并计算它的平方
my_generator_1 = ({i: i ** 2} for i in list01 if isinstance(i, int))

for i in my_generator_1:
    print(i)

