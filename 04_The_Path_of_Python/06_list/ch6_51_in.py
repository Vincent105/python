password = 'deepstone'
ch = input('請輸入字元=')

print('in運算')
if ch in password:
    print('輸入的字元等於密碼')
else:
    print('輸入的字元不等於密碼')    

print('not in 運算')
if ch not in password:
    print('輸入的字元不等於密碼')        
else:
    print('輸入的字元等於密碼')        

fruits = ['apple','banana','watermelon']
fruit = input('請輸入水果名稱：')

if fruit in fruits:
    print('這個水果已經有了')
else:
    fruits.append(fruit)        
    print('水果已經加入清單內')
