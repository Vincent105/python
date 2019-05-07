import car 

my_new_car_1 = car.Car('Japan', 'Toyota', '2016')    
print(my_new_car_1.get_descriptive_name())
my_new_car_1.odometer_reading = 23
my_new_car_1.read_odometer()

my_new_car_2 = car.ElectricCar('USA', 'Tesla', '2016')    
print(my_new_car_2.get_descriptive_name())
