x = range(3)
print(type(x))

for i in range(3):
    print(i)
print('\n')    

for j in range(1,10,2):
    print(j)
print('\n') 

for j in range(10,-10,-2):
    print(j)

number = int(input("請輸入星星數量："))
for time in range(number):
    print("*",end="")