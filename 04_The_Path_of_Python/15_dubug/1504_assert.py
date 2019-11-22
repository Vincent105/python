class Banks():
    # 定義銀行類型
    title = 'Taipei Bank'

    def __init__(self, uname, money):
        self.name = uname
        self.balance = money

    def save_money(self, money):
        try:
            assert money > 0, '存款金額必須大於0'
            self.balance += money
        except AssertionError:
            print("Error:存款金額必須大於0，本次異動並未生效")
        else:
            print("存款", money, "完成")

    def withdraw_money(self, money):
        try:
            assert money > 0, '提款金額必須大於0'
        except AssertionError:
            print("Error:提款金額必須大於0，本次異動並未生效")
        else:            
            try:
                assert money <= self.balance,'帳戶餘額不足無法提款'
            except AssertionError:
                print("Error:提款金額必須大於0，本次異動並未生效")      
            else:                
                self.balance -= money
                print("提款", money, "完成")

    def get_balance(self):
        print(self.name.title(), "目前存款", self.balance)

hungbank = Banks('Wang', 100)
hungbank.get_balance()
hungbank.save_money(-300)
hungbank.get_balance()
hungbank.withdraw_money(700)
hungbank.get_balance()
hungbank.save_money(100)
hungbank.get_balance()