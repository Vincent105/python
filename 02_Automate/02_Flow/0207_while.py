#if 與 while 行為不同
spam = 0
if spam < 5 :
	print('Hello\n')
	spam = spam + 1

spam = 0
while spam < 5 :	
	print('Hello')
	spam = spam + 1	

#while 循環
name = ''

while name != 'your name':
	print('type your name:')
	name = input()
print('Thank you')	
 