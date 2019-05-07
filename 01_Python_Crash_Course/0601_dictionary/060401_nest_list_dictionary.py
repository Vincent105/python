#将列表作为值存储在字典中,在列表中嵌套字典,在字典中嵌套列表甚至在字典中嵌套字典。

#字典列表
alien_0 = {'color': 'green','points': '5'}
alien_1 = {'color': 'yellow','points': '10'}
alien_2 = {'color': 'red','points': '15'}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)

#自動生成
aliens = []	

for alien_number in range(30):
	new_alien = {'color': 'green','points': '5','speed': 'low'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)	

print("Total alien is " + str(len(aliens)) + ".")

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = '10'
		alien['speed'] = 'medium'

for alien in aliens[3:11]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['points'] = '15'
		alien['speed'] = 'fast'	

for alien in aliens[:15]:
	print(alien)

#在字典中儲存列表
pizza = {
	'crust': 'thick',
	'toppings': ['mushroom','extra cheese'],
	}

print("You ordered a " + pizza['crust'] + "-pizza." + "with the following toppings")

for topping in pizza['toppings']:
	print("\t" + topping)

#在字典中儲存列表
favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell']
	}

for name, language in favorite_languages.items():
	print("\n" + name.title() + "s favorite languages are:")
	for language in language:
		print("\t" + language.title())

#在字典中儲存字典
users = {
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
	fullname = userinfo['first'] + " " + userinfo['last']
	location = userinfo['location']
	print("\tFullname: " + fullname)
	print("\tLocation: " + location)
