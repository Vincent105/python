drinks = ['coffee', 'tea', 'wine']
enumerate_drink = enumerate(drinks)
lst = list(enumerate_drink)
print(enumerate_drink)
print(enumerate_drink)
print(lst)

print('============================')
drinks = ('coffee', 'tea', 'wine')
enumerate_drinks = enumerate(drinks)
print(tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks,start=10)
for drink in enumerate_drinks:
    print(drink)

enumerate_drinks = enumerate(drinks,start=10)
for count, enumerate_drink in enumerate_drinks:
    print(count,enumerate_drink)

