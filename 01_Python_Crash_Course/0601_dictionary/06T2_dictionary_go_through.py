rivers = {
	'taiwan': 'a',
	'china': 'b',
	'usa': 'c',
}

rivers['japan'] = 'd'
rivers['korean'] = 'e'

del rivers['korean']

for river,value in rivers.items():
	print(river + " is with " + value)

for river in rivers.keys():
	print(river)	

for value in rivers.values():
	print(value)	


