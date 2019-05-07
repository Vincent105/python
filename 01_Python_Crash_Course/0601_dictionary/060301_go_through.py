use_0 = {
	'username': 'vin',
	'first': 'vincent',
	'last': 'wang',
}

for key, value in use_0.items():
	print("key: " + key)
	print("value: " + value + "\n")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edard': 'c#',
	'phil': 'python',
}

friends = ['phil','sarah']

for name, languages in favorite_languages.items():
	print(name.title() + "'s favorite languages is " + languages.title() + ".")

for name in favorite_languages:
	print(name.title())
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("\tHi,Your favority languages is " + favorite_languages[name].title())
	elif name not in friends:
		print("\tHi,Your favority languages is unknow.")	

#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
	print(name.title())

#遍历字典中的所有值
for language in favorite_languages.values():
	print(language.title())	

#最终的列表可能包含大量的重复项。为剔除重复项，可使用集合（set）。集合 类似于列表，但每个元素都必须是独一无二的：
for language in set(favorite_languages.values()):	
	print(language.title())	

	