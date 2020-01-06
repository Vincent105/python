catNames = []

while True:
	print('Please enter the name of cat ' + str(len(catNames)+1) + ' or enter nothing to quit : ')
	name = input()
	if name =='':
		break
	catNames += [name]
	print(name.title() + ' is added to the catNames list.')

print('The cat name are: ')
for name in catNames:
	print('\t'+ name.title())	