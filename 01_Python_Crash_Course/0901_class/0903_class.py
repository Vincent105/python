class Car():
    """一次模擬汽車的簡單嘗試"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 100

    def fill_gas_tank(self,gas_tank):
        """秀出目前油箱容量"""
        print("Your car's gas_tank is " + gas_tank)

    def get_descritive_name(self):
        long_name = str(self.year) + ' ' + self.model + '' + self.make
        return long_name.title()

    def read_odometer(self):
        print('This car has' + str( self.odometer_reading) + 'mile on it.')    

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback the odometer")       

    def increment(self, miles):
        self.odometer_reading += miles

class Battery():
    """模擬電池"""
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
        
    def descibe_battery_size(self):
        '''列印電瓶大小'''
        print('This car has ' + str(self.battery_size))
    def get_range(self):
        '''列印電瓶對應的續航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:    
            range = 270

        message = 'This car cna go ' + str(range)
        message += ' mile on full charge.'
        print(message)

#創建子類別時，父類別必須包含在當前文件，且父類別必須在子類別之前。
#子類別()內指定父類別名稱   
class ElectricCar(Car):
    """電動車的特殊之處"""
    def __init__(self, make, model, year):
        """初始化父類別屬性"""
        super().__init__(make, model, year)         #幫助父類別與子類別串連。
        self.battery = Battery()                    #定義子類別特有的屬性。

    #def describe_battery(self):                    #將電池容量拿出進行改寫。本段廢棄
    #    """秀出電動車目前電池容量"""
    #    print('This car has ' + str(self.battery_size) + ' battery size.')

    def fill_gas_tank(self,gas_tank):
        """電動車並沒有油箱"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model S',2016)
print(my_tesla.get_descritive_name())
#my_tesla.describe_battery()
my_tesla.battery.descibe_battery_size()
my_tesla.battery.get_range()