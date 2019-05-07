prompt = "Please enter your age: "

price_age = ""
active = True

while active == True:
	price_age = input(prompt)

	if str(price_age) == "quit":
		active = False
	elif price_age < 3:
		print("Your price is $3.")
	elif price_age >= 3 and price_age < 12:
		print("Your price is $10.")	
	elif price_age >= 12:	
		print("Your price is $20.")		
		