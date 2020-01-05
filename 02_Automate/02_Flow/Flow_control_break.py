import random,sys,os,math

# while 循環
name = ''

while name != 'your name':
    print('type your name:')
    name = input()
print('Thank you')


name = ''

while True:
    print('type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')

for i in range(5):
	print(random.randint(1,10)) 

while True:
    print('type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('your response is : ' + response)

 