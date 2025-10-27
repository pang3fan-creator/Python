def fun1(*list1):
    num = 1
    for item in list1:
        print(item)
        num *= item
    return num


list1 = [1, 2, 3, 4]
# 下方传参发生变化，上方形参如何变化？
res = fun1(*list1)
print(res)


# 终端中录入多个数据，存储到一个容器，返回录入的值，如果输入0则结束

def fun2(number):
    # 按照指定的分隔符进行字符串分割，分割后变成列表
    list_new = number.split(",")
    # split函数要求必须给分隔符，分隔符可以是空值字符串
    # list_new = number.split(" ")
    # list_new = number.split()

    return list_new

    # if number != "0":
    #     list1 = list(number)
    #     for item in list1:
    #         if item != ',':
    #             list_new.append(item)
    #     return list_new
    # else:
    #     print("函数停止")
    #     return


list_new = []
number = input("请输入多个内容：")
res = fun2(number)
print(res)
# print(list_new)
