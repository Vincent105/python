def show_magicians(names):
	for name in names:
		print("Greeting:" + name.title())

def make_great(magicians,magicians_greeteds):
	while magicians:
		current_magician = magicians.pop()
		print("Greeting:" + current_magician.title())  
		magicians_greeteds.append(current_magician)

def make_great_2(magicians,magicians_greeteds):
	while magicians:
		current_magician = magicians.pop()
		print("Greeting:!!!!!!!!!!!!1" + current_magician.title())  
		magicians_greeteds.append(current_magician)		

def greeted(magicians_greeteds):
	for magicians_greeted in magicians_greeteds:
		print("Greeted:" + magicians_greeted)

magicians = ['vincent','esther','john']
magicians_greeteds = []		

print(magicians)
make_great(magicians[:],magicians_greeteds)
print(magicians)

print(magicians)
make_great_2(magicians,magicians_greeteds)
print(magicians)
