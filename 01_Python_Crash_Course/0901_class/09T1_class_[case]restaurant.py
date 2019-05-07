class Restaurant():
    '''展示餐廳名稱、類型、目前營業狀態'''
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name.title()) 
        print('Restaurant type is ' + self.cuisine_type.title()) 

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open now.') 

    def close_restaurant(self):
        print(self.restaurant_name.title() + ' is close now.')

    def read_number_served(self):
        """列印至金服務顧客數量"""
        print('This restaurant has ' + str(self.number_served) + ' customers served.')        

    def set_number_served(self, customers):
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print('you can not change the served number below current.')    

    def increment_number_served(self, tokens):
        if tokens >= 0:
            self.number_served += tokens
        else:
            print('you can not change the served number below zero.')    

class IceCreamStand():
    '''展示餐廳名稱、類型、目前營業狀態'''  
    def __init__(self, restaurant_name, cuisine_type):
        super().Restaurant(restaurant_name, cuisine_type)

    def flavors(self, flavors):
        print(self.flavors)

restaurant_1 = Restaurant('noodlemix','chinese food')
restaurant_2 = Restaurant('foodpanda','food deliver')

print(restaurant_1.restaurant_name.title() + ' is ' + restaurant_1.cuisine_type)
print(restaurant_2.restaurant_name.title() + ' is ' + restaurant_2.cuisine_type)

restaurant_1.open_restaurant()
restaurant_1.close_restaurant()
restaurant_2.open_restaurant()
restaurant_2.close_restaurant()
restaurant_1.read_number_served()
restaurant_1.number_served = 2
restaurant_1.read_number_served()
restaurant_1.set_number_served(1)
restaurant_1.read_number_served()
restaurant_1.set_number_served(10)
restaurant_1.read_number_served()
restaurant_1.increment_number_served(100)
restaurant_1.read_number_served()
restaurant_1.increment_number_served(-100)
restaurant_1.read_number_served()