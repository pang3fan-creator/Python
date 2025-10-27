"""
彩票：双色球
    红色：6个  1--33之间的整数   不能重复
    蓝色：1个  1--16之间的整数
    1) 随机产生一注彩票(列表(前六个是红色，最后一个蓝色))

    2) 在终端中录入一支彩票
    要求：满足彩票的规则.  not in
    (以上内容是2个需求，一个是随机，一个是录入)

"""
import random

# 1.随机产生一注彩票
list_ticket = []

while len(list_ticket) < 6:
    number = random.randint(1, 33)
    if number not in list_ticket:
        list_ticket.append(number)

list_ticket.append(random.randint(1, 16))
print(list_ticket)

# 2) 在终端中录入一支彩票
list_ticket = []

while len(list_ticket) < 6:
    number = int(input("请输入第" + str(len(list_ticket) + 1) + "个红球号码:"))

    if number in list_ticket:
        print("号码已经存在，请重新输入")
    elif number < 1 or number > 33:
        print("号码不在范围内，请输入1~33之间的数字")
    else:
        list_ticket.append(number)

while len(list_ticket) < 7:
    number = int(input("请输入蓝球号码:"))

    if number < 1 or number > 16:
        print("号码不在范围内，请输入1~16之间的数字")
    else:
        list_ticket.append(number)

print(list_ticket)
