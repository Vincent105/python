car1 = ['toyota', 'nissan', 'honda']
car2 = ['ford', 'audi', 'tesla']

print('原本元素為:',car1)
print('原本元素為:',car2)
car1.append(car2)
print('合併後元素為:',car1)

car3 = ['toyota', 'nissan', 'honda']
car4 = ['ford', 'audi', 'tesla']

print('原本元素為:',car3)
print('原本元素為:',car4)
car3.extend(car4)
print('合併後元素為:',car3)

sc = [['Vincent', 80, 100, 88, 0],
      ['Esther', 100, 90, 99, 0],
     ]

sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])

print(sc[0])
print(sc[1])