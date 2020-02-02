# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k,v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total))

while True:
	print('Enter a name of stuff : (blank to quit)')
	name = input()
	if name == '':
		break
	if name in stuff:
		print(name + "'has the number is " + str(stuff[name]) + '.') 
	else:
		print('I do not have information for ' + name)
		print("what's you have?")
		addNumber = input()
		stuff[name] = int(addNumber)
		print("Databas updated!!")

displayInventory(stuff) 