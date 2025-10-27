"""
创建函数,根据课程阶段计算课程名称

"""


def calc_name(number):
    dict_course = {
        "一": "Python语言核心编程",
        "二": "Python高级软件技术",
        "三": "Web全栈",
        "四": "人工智能"
    }

    if number in dict_course:
        # 当函数中没有return 或者return 没有数据 的时候默认返回none
        # 等价于 return none
        # return 可以退出函数
        return dict_course[number]
        # print("梭哈") #不执行的


number = input("请输入课程阶段数：")
name = calc_name(number)
print(name)
