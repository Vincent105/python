birthdays = {'vincent': '0917','esther': '0314'}

while True:
	print('Enter a name : (blank to quit)')
	name = input()
	if name == '':
		break
	if name in birthdays:
		print(name + "'s birthday is " + birthdays[name] + '.') 
	else:
		print('I do not have birthday information for ' + name)
		print("what's their birthday?")
		bday = input()
		birthdays[name] = bday
		print("Databas updated!!")
