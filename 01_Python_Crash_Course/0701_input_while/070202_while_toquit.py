prompt = "\nTell me something,and I will repeat it to you"
prompt += "\nEnter quit to end this program: "

message = ""

while message != "quit": 
	message = input(prompt)

	if message != 'quit':
		print(message)
 