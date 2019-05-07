prompt = "\nPlease enter the source that you like"
prompt += "\nEnter 'quit' to quit enter:"

source = ""

while True:
	source = input(prompt)

	if source == 'quit':
		break
	else:	
		print(source)