store = ("Deepstone")
products = ['mango', 'apple', 'watermelon', 'banana']
cart = []
print(store)
print(products,'\n')

while True:
    msg = input('buy(q=quit):')    
    if msg == 'q' or msg == 'Q':
        break
    else:
        if msg in products:
            cart.append(msg)
print(cart)            