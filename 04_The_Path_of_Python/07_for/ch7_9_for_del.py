fruits = ['apple', 'banana', 'mango', 'watermelon']
print('目前水果', fruits)

for fruit in fruits[:]:
    fruits.remove(fruit)
    print('目前刪除的是%s'%fruit)
    print('目前剩下的是%s'%fruits)