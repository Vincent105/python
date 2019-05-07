def city_country(city,country):
	word = '"' + city.title() + "," + country.title() + '"'
	print(word)
	return word

city_country('Santiago','Chile')
city_country('taipei','taiwan')
city_country(city='tyoko',country='japan')

def make_album(singer,ablum,number=''):
	music = {'singer': singer,'ablum': ablum}
	if number:
		music['number'] = number
	return music

music = make_album('vincent','yes','3')
music1 = make_album('esther','no','5')
music2 = make_album('john','none')
print(music['singer'] + " " + music['ablum'])
print(music1)
print(music2)

while True:
	print("\nPlease tell me your favorite singer?")
	print("(enter 'q' at any time to quit)")
	f_singer = input("Singer: ")
	if f_singer == 'q':
		break
	f_ablum = input("Ablum: ")
	if f_ablum == 'q':
		break	

	love_name = make_album(f_singer,f_ablum) 	
	print (love_name)