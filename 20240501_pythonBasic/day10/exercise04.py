"""
银行账户类 Bank 2个属性: 账号 和 余额
函数 deposit 向指定的账户存入指定金额
函数 withdraw 从指定的账户取出指定金额（如果余额不够不能取）
函数 get_balance 获取账户金额
使用实例：
account  = Bank("123456",1000)
account.deposit(500)
account.withdraw(300)
account.get_balance() 1200
"""

class Bank:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        # if money > 0 and money <= self.balance:
        if 0 < money <= self.balance:
            self.balance -= money
        elif money > self.balance:
            print("余额不足")
        else:
            print("嘿嘿嘿~")

    def get_balance(self):
        # print(self.balance)
        return self.balance


acc = Bank("123456", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())  # 1200
