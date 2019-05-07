#如果你只想执行一个代码块，就使用if-elif-else 结构；
#如果要运行多个代码块，就使用一系列独立的if 语句。

age	 = 17 
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registed to vote yet?")
else:
	print("You are too young to vote!")		
	print("Please register to vote as soon as you turn 18!")

age = 12 
if age < 4:
	print("Your admission is $0.")
elif age <= 12:
	print("Your admission is $1.")
elif age < 18:
	print("Your admission is $5.")	
else:
	print("Your admission is $10.")	

age = 12 
if age < 4:
	price = 0
elif age <= 12:
	price = 1
else:
	price = 10

print ("Your admission is $" + str(price) + ".")	
