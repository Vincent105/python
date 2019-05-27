fruits = {
    'apple': 10,
    'banana': 20
}
#get
price_for_apple = fruits.get('apple')
print(price_for_apple)

price_for_orange = fruits.get('orange')
print(price_for_orange)

price_for_mango = fruits.get('mango',100)   #如果找不到就給予預設值
print(price_for_mango)

print(fruits)

#setdefault 將改變字典
price_for_apple = fruits.setdefault('apple')
print(price_for_apple)

price_for_orange = fruits.setdefault('orange')
print(price_for_orange)

price_for_mango = fruits.setdefault('mango',100)   #如果找不到就給予預設值
print(price_for_mango)

print(fruits)

