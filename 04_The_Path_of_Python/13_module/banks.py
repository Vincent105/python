class Banks():
    def __init__(self, uname):
        self.__name = uname  # 設定私有屬性，避免外部修改
        self.__balance = 0
        self.__title = 'Taipei Bank'

    def save_money(self, money):
        self.__balance += money
        print("存款:", money, " 成功。")

    def withdraw_money(self, money):
        self.__balance -= money
        print("提款:", money, " 成功。")

    def get_balance(self):
        print("目前餘額：", self.__balance)

    def bank_title(self):
        return self.__title


class Shilin_Banks(Banks):
    def __init__(self, uname):
        self.title = "shlin"
    def bank_title(self):
        return self.title       
