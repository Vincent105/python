# Basic method
spam = 'Hello world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

# isX method
print(spam.isupper())
print(spam.islower())
print('Hello'.upper().islower())
print('Hello'.isalpha())
print('Hello'.isalnum())
print('Hello'.isdecimal())
print(' '.isspace())
print('Hello'.istitle())

while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for your age.')	

while True:
	print('select a password:')
	password = input()
	if password.isalnum():
		break
	print('password can only have letters and numbers')		