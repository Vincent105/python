allGuests = {
	'vincent': {'apple': 3,'banana':4},
	'esther': {'sanwitch': 7,'banana':4},
	'john': {'cups': 1,'pies':6}
	}

def totalBrought(guests,item):
	numberBrought = 0 
	for n,i in guests.items():
		numberBrought += i.get(item,0)	
	return(numberBrought)
 
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apple')))
print(' - banana ' + str(totalBrought(allGuests, 'banana')))
print(' - cups ' + str(totalBrought(allGuests, 'cups')))
print(' - pies ' + str(totalBrought(allGuests, 'pies')))

print(allGuests.items())


