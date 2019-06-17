import random

fruits = ['apple', 'watermelon', 'mango']
print(random.choice(fruits))

for i in range(10):
    print(random.choice([1, 2, 3, 4, 5, 6]), end=',')

poker = ['2','3','4','5','a','b','c']

for i in range(3):
    random.shuffle(poker)
    print(poker)


lotterys = random.sample(range(1, 50), 7)
special = lotterys.pop()

print('樂透號碼：',end='')
for lottery in sorted(lotterys):
    print(lottery,end=',')
print('特別號碼%s:'%special)    


testnum = random.uniform(3, 7)
print(testnum)

testnum = random.random()
print(testnum)