prompt = "\nPlease enter the source that you like"
prompt += "\nEnter 'quit' to quit enter:"

source = ""

while source != 'quit':
	source = input(prompt)

	if source == 'quit':
		print(source)
