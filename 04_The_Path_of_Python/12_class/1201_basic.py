class Bank():
    '''define bank'''
    bankname = 'ctbank'

    def __init__(self, uname, money):
        self.name = uname
        self.balance = money

    def save_money(self, money):
        self.balance += money
        print("存款 " + str(money) + ' 完成')

    def withdraw_money(self, money):
        self.balance -= money
        print("取款 " + str(money) + ' 完成')

    def get_balance(self):
        print(self.name.title() + "目前餘額是：" + str(self.balance))

    def motto(self):
        return 'we serve the best.'


userbank = Bank('vincent', 100)
print(userbank.bankname, userbank.motto(),'\n')
userbank.get_balance()
userbank.save_money(500)
userbank.get_balance()
userbank.withdraw_money(100)
userbank.get_balance()

userbank_2 = Bank('esther', 10100)
print(userbank_2.bankname, userbank_2.motto(),'\n')
userbank_2.get_balance()
userbank_2.save_money(500)
userbank_2.get_balance()
userbank_2.withdraw_money(100)
userbank_2.get_balance()