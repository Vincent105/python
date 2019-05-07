#必须在函数定义中将接纳任意数量实参的形参放在最后。

def make_pizza(size,*toppings):
	"""概述要制作的比萨"""
	print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(12,'pepperoni')
make_pizza(13,'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first,last,**user_info):
	profile = {}

	profile['first_name'] = first
	profile['last_name'] = last

	for key,value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print('\n')
print(user_profile)



