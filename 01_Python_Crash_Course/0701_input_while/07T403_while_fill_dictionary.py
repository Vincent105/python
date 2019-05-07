responses = {}

active = True

while active:
	name = input("What's your name?")
	place = input("If you could visit one place in the world, where would you go?")
	
	responses[name] = place

	repeat = input("Would you like to keyin another respond? (yes/ no)")
	if repeat == 'no':
		active = False

print("\n--- Results ---")			
for name, plcae in responses.items():
	print(name.title() + " would like to go to " + place + ".")