x = None
print(x)

print('判斷字元輸入類型')
ch = input('請輸入字元')

if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
    print('這是大寫子母')
elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
    print('這是小寫子母')
elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
    print('這是數字')    
else:
    print('這是特殊字元')    




