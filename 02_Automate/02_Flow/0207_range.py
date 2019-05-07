#for while 產出range效果
print('My name is V1')
for i in range(5):
	print('Vincent' + ' (' + str(i) + ')')
	continue

print('My name is V2')
i = 0
while i < 5:
	print('Vincent' + ' (' + str(i) + ')')
	i += 1	

#利用range及for，0加到100
total = 0

for sumup in range(101):
	total = total + sumup
print(total)	

#range的參數
for i in range(12,16):
	print(i)

for i in range(0,16,3):
	print(i)	

for i in range(5,-1,-1):
	print(i)		

