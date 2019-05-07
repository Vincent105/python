print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print('howdyyyy' not in ['hello', 'hi', 'howdy', 'heyas'])

spam = ['hello', 'hi', 'howdy', 'heyas']
print('hi' in spam)
print('howdy' not in spam)

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('please enter your name of pet: ')
name = input()

if name in myPets:
	print('yes this is your pet name.')
else:	
	print('nope')

