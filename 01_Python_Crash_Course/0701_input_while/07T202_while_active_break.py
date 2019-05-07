prompt = "\nPlease enter the source that you like"
prompt += "\nEnter 'quit' to quit enter:"

source = ""

active = True
while active == True:
	source = input(prompt)

	if source == 'quit':
		active = False
	else:	
		print(source)