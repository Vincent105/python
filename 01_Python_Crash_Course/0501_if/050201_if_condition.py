cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())	

#檢查條件是否相等
car = 'bmw'				#將值賦予變數(一个等号是陈述)
print(car =='bmw')		#確認條件是否相等	(两个等号是发问)
print(cars =='audi')

#檢查條件是否相等(大小写不同的值视为不相等)
print(car == 'bmw')
print(car == 'BMW')
car = 'BMW'
print(car.lower() == 'bmw')	#轉成小寫
print(car)

#檢查條件是否相等(大小写不同的值视为不相等)
request = "mushroom"
if request != "anchovies":
	print("Hold the anchovies")
else:
	print("Hold the mushroom")

#比較數字
age = 18
print(age == 18)

answer = 17
if answer != 42:
	print("That is not a clear answer")
print(17 >= 17)
print(17 > 17)
print(16 < 17)
print(16 <= 17)

#使用 and 檢查多個條件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print((age_0 >= 21) and (age_1 >= 22))

#使用 or 檢查多個條件
print(age_0 >= 21 or age_1 >= 21)

#檢查特定值是否包含在列表內
request = ['mushroom','onions','pinapple']
print('mushroom' in request)
print('pepperroni' in request)

#檢查特定值是否不包含在列表內
banned_users = ['Vincent','Esther','Frank']
users = 'King'
if users not in banned_users:
	print(users.upper() + ",You are not in the banned users list")
	