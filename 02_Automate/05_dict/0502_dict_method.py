spam = {'color': 'red','age': '42'}

for v in spam.values():
	print(v)

for y in spam.keys():
	print(y)	

for i in spam.items():
	print(i)

for key,value in spam.items():
	print('key: ' + key + ' value: ' + value)		

print(spam.keys())
print(list(spam.keys()))

print('color' in spam.keys())
print('red' in spam.values())
print('color' not in spam.keys())
print('red' not in spam.values())

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups',0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('banana',0)) + ' cups.')	#get()方法返回的默认值是 0。

spam = {'name': 'vincent','age': '20'}
if 'color' not in spam:
	spam['color'] = 'black'

print(spam)
spam.setdefault('color_2','white')					#除非key值不存在，才會給予預設值；若存在這不進行覆蓋。
print(spam.setdefault('color_2','white'))
print(spam)
print(spam.setdefault('name','esther'))
print(spam)

#計算字串出現次數，並導入pprint module
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character,0)
	count[character] += 1

pprint.pprint(count)	

