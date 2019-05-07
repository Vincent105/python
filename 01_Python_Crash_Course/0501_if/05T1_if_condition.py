string_1 = 'King'	
string_2 = 'John'	

if string_1 != string_2:
	print(string_1.upper() + " " + string_2.lower() + " " + "are not equal")
else:
	print(string_1 + " " + string_2 + " " + "are equal")	

number_1 = 20 
number_2 = 10

if number_1 == number_2:
	print(str(number_1) + " is equal to " + str(number_2))
else:	
	print(str(number_1) + " is not equal to " + str(number_2))

if number_1 >= number_2:
	print(str(number_1) + " >= " + str(number_2))
else:	
	print(str(number_1) + " is not >= " + str(number_2))	

if number_1 <= number_2:
	print(str(number_1) + " <= " + str(number_2))
else:	
	print(str(number_1) + " is not <= " + str(number_2))	

if number_1 >=20 and number_2 >=20:
	print(str(number_1) + " and " + str(number_2) + " is >=20")
else:	
	print(str(number_1) + " and " + str(number_2) + " is not >=20")

if number_1 >=20 or number_2 >=20:
	print(str(number_1) + " or " + str(number_2) + " is >=20")
else:	
	print(str(number_1) + " or " + str(number_2) + " is not >=20")	

cars = ['bmw','toyota','audi']
if 'bmw' in cars:
	print("Yes")
if 'benz' not in cars:
	print("benz is not in the car list")









