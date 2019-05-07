# 轉義字符( \ )
spam = 'Say hi to Bob\'s mother'	#單引號(\')
print(spam)
spam = 'Say hi to Bob\"s mother'	#雙引號(\")
print(spam)
spam = 'Say hi to Bob\ts mother'	#製表符(\t)
print(spam)
spam = 'Say hi to Bob\ns mother'	#換行符(\n)
print(spam)
spam = 'Say hi to Bob\\s mother'	#斜線符(\\)
print(spam)
print(r'spameqe\qeqweeq\\e')		#原始字符串顯示(r)

print('''Dear Alice,				

Eve's cat has been arrested for catnapping, cat burglary,\t'' and extortion.

Sincerely,

Bob''')								#三重引號多行字符串(r)

spam = 'Hello world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])
