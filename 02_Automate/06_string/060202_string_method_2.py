# startswith() 和 endswith
print('Hello world!'.startswith('Hello'))
print('Hello world!'.startswith('hello'))
print('Hello world!'.startswith('world!'))
print('Hello world!'.endswith('world!'))
print('Hello world!'.endswith('Hello'))
print('Hello world!'.endswith('Hello world!'))

# join()
print(','.join(['cats','rats']))
print(' '.join(['My','name','is','Vincent']))
print('ABC'.join(['My','name','is','Vincent']))

# split()
print('My name is Vincent'.split())
print('MyABCnameABCisABCVincent'.split('ABC'))
print('My name is Vincent'.split('m'))

# split() 依造換行符號。
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))

# rjust() center() ljust()進行對齊
print('Hello world'.rjust(10))

print('Hello world'.rjust(20))
print('Hello world'.center(20))
print('Hello world'.ljust(20))

print('Hello world'.rjust(20,'-'))	#輸入填充字符
print('Hello world'.center(20,'-'))
print('Hello world'.ljust(20,'-'))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def printPicnic(itemsDict, leftWidth, rightWidth):
	print('PICINIC ITEMS'.center(leftWidth + rightWidth,'|'))
	for v,k in itemsDict.items():
		print(str(k).ljust(leftWidth,'.') + str(v).rjust(rightWidth))

printPicnic(picnicItems, 12, 5)		
printPicnic(picnicItems, 20, 6)

#strip()、 rstrip()和 lstrip()删除空白字符
spam = ' Hello World '
print(spam.rstrip())
print(spam.lstrip())
print(spam.strip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

#用pyperclip模組複製貼上字符串
import pyperclip

pyperclip.copy('Hello world!')
print(pyperclip.paste())


