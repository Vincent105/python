class Car():
    """一次模擬汽車的簡單測試"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """列印汽車里程數"""
        print('This car has ' + str(self.odometer) + ' miles on it.')

    def update_odometer(self, mileage):      #透過method修改屬性值
        """修改里程數值"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You can not roll back an odometer!')    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer += miles
        else:
            print('You can not roll back an odometer!')    

my_new_car = Car('audi', 'a4', 2006)
print(my_new_car.get_descriptive_name())

my_new_car.odometer = 23        #直接訪問屬性進行修改。
my_new_car.read_odometer()

my_new_car.update_odometer(50)        #直接訪問屬性進行修改。
my_new_car.read_odometer()

n_mile = int(input ('第一次使用了多少里程：'))
my_new_car.increment_odometer(n_mile)
my_new_car.read_odometer()

n_mile = int(input ('第二次使用了多少里程：'))
my_new_car.increment_odometer(n_mile)
my_new_car.read_odometer()
