print(4 % 3)
print(6 % 3)

#運用%取得餘數，判斷奇數或偶數
number = input("Enter a number,and I will tell you odd or even:")
number = int(number)

if number % 2 == 0:
	print("\nThe number: " + str(number) + " is even." )
else:
	print("\nThe number: " + str(number) + " is odd." )
