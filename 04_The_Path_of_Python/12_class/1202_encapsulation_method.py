class Bank():
    def __init__(self, uname):
        self.__name = uname                 #設定私有屬性，避免外部修改
        self.__balance = 0
        self.__bankname = 'Taipei Bank'
        self.__rate = 30
        self.__service_charge = 0.01

    def save_money(self, money):
        self.__balance += money
        print("存款:" , money , " 成功。")

    def withdraw_money(self, money):
        self.__balance -= money
        print("提款:" , money , " 成功。")

    def get_balabce(self):
        print("目前餘額：" , self.__balance)

    def usa_to_taiwan(self,usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):
        return int(usa_d * self.__rate*(1 - self.__service_charge))

hungbank = Bank('vincent')
hungbank.get_balabce()
hungbank.__balance = 1000000        
hungbank.get_balabce()
hungbank._Bank__balance = 1000000        #透過使方法可串改私有屬性
hungbank.get_balabce()
usadollor = 50
print(usadollor,hungbank.usa_to_taiwan(usadollor))

hungbank._Bank__cal_rate(50)