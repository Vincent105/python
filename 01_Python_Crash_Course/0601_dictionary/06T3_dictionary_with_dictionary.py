#基本字典 - 實作
users = {
	'vincent': {
		'first': 'vincent',
		'last': 'wang',
		'location': 'taipei',
		},
	'esther': {
		'first': 'esther',
		'last': 'huang',
		'location': 'taipei',
		},
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},	
	}
 
for username,userinfo in users.items():
	print("\nUsername: " + username)
	fullname = userinfo['first'] + userinfo['last']
	location = userinfo['location']
	print("\tFullname: " + fullname)
	print("\tLocation: " + location)

#字典列表 - 實作
animals1 = {
	'type': 'mouse',
	'master': 'vincent', 
}

animals2 = {
	'type': 'cat',
	'master': 'esther', 
}

animals3 = {
	'type': 'fish',
	'master': 'john', 
}

pets = [animals1,animals2,animals3]

for pet in pets:
	print(pet)

#在字典中儲存列表
favorite_places = {
	'vincent': ['jp','usa','tw'],
	'esther': ['tw'],
	'john': ['fr','jp','cn'],
	}

for name,place in favorite_places.items():
	print("\n" + name + "'s favorite place are:")
	for place in place:
		print("\t" + place)

#在字典中儲存列表
number_detail = {
	'esther': ['22','33','44'],
	'vincent': ['25','11','0'],
	'john': ['35'],
	'andy': [1,2,3],
}

for name, number in number_detail.items():
	print("\n" + name +"'s favorite numbers are:")
	for number in number:
		print("\t" + str(number))

#在字典中儲存字典
cities={
	'Taipei': {
	'country': 'tw',
	'population': '1111',
	'fact': 'fast'
	},
	'shiha': {
	'country': 'cn',
	'population': '2222',
	'fact': 'medium'
	},
	'tyoko': {
	'country': 'jp',
	'population': '3333',
	'fact': 'low'
	},
}		

for city, info  in cities.items():
	print("\nCity:" + city)
	country = info['country']
	population = info['population']
	fact = info['fact']
	print("\t" + country)
	print("\t" + population)
	print("\t" + fact)
