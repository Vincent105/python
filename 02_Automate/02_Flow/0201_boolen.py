# Boolean mean True or False
spam = True
print(spam)

print('42 = 42 ?:' + str(42 == 42))
print('42 = 99 ?:' + str(42 == 99))
print('2 != 3 ?:' + str(2 != 3))
print('2 != 2 ?:' + str(2 != 2))
print("'hello' == 'hello' ?:" + str('hello' == 'hello'))
print("'Hello' == 'hello' ?:" + str('Hello' == 'hello'))
print("'dog' == 'cat' ?:" + str('dog' == 'cat'))
print("'True' == 'True' ?:" + str(True == True))
print("'True' != 'False' ?:" + str(True != False))
print("40 == 40.0 ?:" + str(40 == 40.0))
print("42 == '42 ?:" + str(42 == '42'))
print("42 < 100 ?:" + str(42 < 100))
print("42 > 100 ?:" + str(42 > 100))

eggCount = 42
print("eggCount= 42;eggCount>= 42 ?:" + str(eggCount >= 42))

name = ''
password = ''

if name == 'Mary':
	print('Hello Mary.')
if password == 'swordfish':
	print('Access granted.')	
else:
	print('Wrong password.')
 