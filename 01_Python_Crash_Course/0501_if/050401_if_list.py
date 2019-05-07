#使用IF檢查列表中的特定元素
requests = ['apple','banana','mango']

for request in requests:
	print("Adding " + request + ".")

print("\nFinish!")

for request in requests:
	if request == 'banana':
		print("Sorry,we don't have banana.")
	else:	
		print("Adding " + request + ".")
	
print("\nFinish!Again")

#確認列表是否為空
inputtexts = []

if inputtexts:								#將在列表至少包含一個元素時返回True;列表為空返回False
	for inputtext in inputtexts:
		print("Adding " + inputtext)
	print("Finish adding to your pizza.")	
else:
	print("Are you want a plain pizza ")

#使用多個列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
					 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + " to pizza.")
	else:
		print("Sorry,we don't have " + requested_topping + ' .')

print("Finish adding your pizza!")			

