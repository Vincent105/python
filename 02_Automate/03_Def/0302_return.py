import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber == 2:
		return 'It is decidedly so'	
	elif answerNumber == 3:
		return 'Yes'
	elif answerNumber == 4:
		return 'No'		
	else:
		return 'No idea'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

# print(getAnswer(random.randint(1,9)))  上述三行可直接改寫

spam = print('hello')
print(None == spam)

print('hello',end = '')
print('vicnent')
print(end ='\n')