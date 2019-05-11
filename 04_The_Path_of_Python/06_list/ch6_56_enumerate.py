drinks = ['cofee', 'tea', 'water']
enumerate_drink = enumerate(drinks)

print(enumerate_drink)
print(type(enumerate_drink))

enumerate_drink = enumerate(drinks)
print('索引從0開始',list(enumerate_drink))
enumerate_drink = enumerate(drinks,start = 10)
print('索引從10開始:',list(enumerate_drink))

enumerate_drink = enumerate(drinks)
print('索引從0開始',tuple(enumerate_drink))
enumerate_drink = enumerate(drinks,start = 10)
print('索引從10開始:',tuple(enumerate_drink))

enumerate_drink = enumerate(drinks)
print('索引從0開始',set(enumerate_drink))
enumerate_drink = enumerate(drinks,start = 10)
print('索引從10開始:',set(enumerate_drink))