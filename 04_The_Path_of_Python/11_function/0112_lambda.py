square = lambda x: x**2
print(square(2))

product = lambda x, y: x * y
print(product(3,2))

#case 1
def func(b):
    return lambda x: 2 * x + b

linear = func(5)    
print(linear(10))

linear2 = func(15)    
print(linear2(100))

#case 2
'''
def mycar(cars,func):
    for car in cars:
        print(func(car))

def wdcar(carbrand):
    return "My dream car is " + carbrand.title()


dreamcars = ['porsche','maserati','rolls royce']
mycar(dreamcars, wdcar)
'''
#case 3

def mycar(cars,func):
    for car in cars:
        print(func(car))


dreamcars = ['porsche','maserati','rolls royce']
mycar(dreamcars, lambda carbrand:"My dream car is " + carbrand.title())