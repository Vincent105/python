class Father():
    def __init__(self):
        self.__address = "羅斯福路"

    def getaddr(self):
        return self.__address

    def downtown(self):
        print('live in taipei')


class Son(Father):
    pass


hung = Father()
hung.downtown()
print(hung.getaddr())
wang = Son()
wang.downtown()
print(wang.getaddr())


class Bank():
    def __init__(self, uname):
        self.__name = uname  # 設定私有屬性，避免外部修改
        self.__balance = 0
        self.__bankname = 'Taipei Bank'
        self.__rate = 30
        self.__service_charge = 0.01

    def bank_title(self):
        return self.__bankname

    def save_money(self, money):
        self.__balance += money
        print("存款:", money, " 成功。")

    def withdraw_money(self, money):
        self.__balance -= money
        print("提款:", money, " 成功。")

    def get_balabce(self):
        print("目前餘額：", self.__balance)

    def usa_to_taiwan(self, usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):
        return int(usa_d * self.__rate*(1 - self.__service_charge))
    

class Shilin_Banks(Bank):
    def __init__(self,uname):
        super().__init__(uname)
        self.bankname ='Shilin_Banks'

    def bank_title(self):
        return self.bankname




wang = Shilin_Banks('wang')
wang.get_balabce()
wang.save_money(100)
wang.withdraw_money(100)
wang.get_balabce()
print(wang.bank_title())