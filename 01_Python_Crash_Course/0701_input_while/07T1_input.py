car = input("What's car do you want: ")
print("Let me see if I can find you a " + car)

number = input("How people will attend for dinner?: ")
number = int(number)

if number > 8:
	print("We don't have seats!")
else:	
	print("We have seats for " + str(number) + " people.")	

number = ("Enter a number")
number += ("And I will show u if it can divide by 10: ") 

number = input(number)
number = int(number)

if number % 10 == 0 :
	print("Yes")
else:	
	print("No")	

