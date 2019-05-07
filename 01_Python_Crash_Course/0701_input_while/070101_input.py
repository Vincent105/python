#基本input
name = input("Enter your name:")
print("Hello," + name)

#基本input
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello," + name + "?")

age =input("How old are you?")
age = int(age)
print("Your age is larage or equal to 18?" + str(age >= 18))

# 使用Int來取得數值
height = input("How tall are you,in inch?")
height = int(height)

if height >= 36:
	print("\nYou are tall enough to ride")
else:
	print("\nYou'll be able to ride when you're a little older.")	

