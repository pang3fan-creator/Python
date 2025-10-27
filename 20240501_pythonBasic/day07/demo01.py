def calc_discount(account_type, money):
    # if account_type == "vip":
    #     # 条件表达式(三元/三目运算符)
    #     # 语法：结果1 if 条件 else 结果2
    #     # 如果满足条件则返回结果1，否则返回结果2
    #     return "享受85折扣" if money < 500 else "享受8折扣"
    # else:
    #     return "享受9折扣" if money > 800 else "原价购买"

    if account_type == "vip":
        return "享受85折扣" if money < 500 else "享受8折扣"

    return "享受9折扣" if money > 800 else "原价购买"


account_type = input("请输入账户类型：")
money = float(input("请输入消费金额："))

discount = calc_discount(account_type, money)
print(discount)
