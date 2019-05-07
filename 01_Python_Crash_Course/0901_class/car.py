"""一個可用於表示汽車的class"""
class Car():
    """汽車模擬"""
    def __init__(self, make, model, year):
        """初始化屬性"""
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回完整名稱"""        
        long_name = str(self.make) + ' ' + self.model + ' ' + str(self.year)
        return long_name.title()

    def read_odometer(self):
        """讀取里程數"""
        print('This car has ' + str(self.odometer_reading) + ' meter on it.')

    def update_odometer(self, mile):
        """檢核里程數：若比目前值大則接受異動"""
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print('You can not roll back the odometer.')    

    def increment_odometer(self, mile):
        self.odometer_reading += mile

class Battery():
    """存放有關電池敘述的class"""
    def __init__(self, battery_size=70):
        """初始化電池屬性"""
        self.battery_size = battery_size

    def descibe_battery(self):
        """列印電池屬性的敘述"""
        print('The battery size is ' + str(self.battery_size) + '.')

    def get_battery(self):
        if  self.battery_size == 70:
            battery_range = 240
        elif self.battery_size == 80:             
            battery_range = 270            

        message = 'This car go ' + str(battery_range)            
        message += ' miles on a full charge.'
        print(message)

class ElectricCar(Car):
    """存放電動汽車特殊屬性"""
    def __init__(self, make, model, year):
        """初始化父類屬性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    