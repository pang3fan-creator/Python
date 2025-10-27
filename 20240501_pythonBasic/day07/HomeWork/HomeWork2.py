"""
    定义函数,计算折扣
    account_type = input("请输入账户类型：")
    money = float(input("请输入消费金额："))
    if account_type == "vip":
        if money < 500:
            print("享受85折扣")
        else:
            print("享受8折扣")
    else:
        if money > 800:
            print("享受9折扣")
        else:
            print("原价购买")
"""


def calc_discount(account_type, money):
    # if account_type == "vip":
    #     if money < 500:
    #         print("享受85折扣")
    #     else:
    #         print("享受8折扣")
    # else:
    #     if money > 800:
    #         print("享受9折扣")
    #     else:
    #         print("原价购买")

    if account_type == "vip":

        if money < 500:
            return "享受85折扣"
        else:
            return "享受8折扣"

    else:
        if money > 800:
            return "享受9折扣"
        else:
            return "原价购买"

# 15分钟 10：12继续
account_type = input("请输入账户类型：")
money = float(input("请输入消费金额："))

discount = calc_discount(account_type, money)
print(discount)
