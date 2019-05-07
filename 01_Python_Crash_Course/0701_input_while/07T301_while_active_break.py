prompt = "Please enter your age: "

price_age = ""

while str(price_age) != "quit":
	price_age = input(prompt)

	if str(price_age) != "quit":
		price_age = int(price_age)
		if price_age < 3:
			print("Your price is $3.")
		elif price_age >= 3 and price_age < 12:
			print("Your price is $10.")	
		elif price_age >= 12:	
			print("Your price is $20.")		