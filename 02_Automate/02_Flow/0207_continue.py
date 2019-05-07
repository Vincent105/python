#遇到break 會馬上跳回循環開始處:重新循環求值。

while True:
	print('type your name')
	name = input()
	if name != 'joe':
		continue
	print('Hello, Joe. What is the password? (It is a fish.)')
	password = input()
	if password == 'swordfish':
		break
print('Access granted')

