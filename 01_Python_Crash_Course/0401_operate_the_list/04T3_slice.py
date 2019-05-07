my_foods = ['pizza', 'falafel', 'carrot cake','beef','pork']
print("The first three items in the list are:" + str(my_foods[:3]))
print("Three items from the middle of the list are:" + str(my_foods[1:4]))
print("The last three items in the list are:" + str(my_foods[-3:]))

your_foods =my_foods[:]
my_foods.append('apple')
your_foods.append('mango')

for my_food in my_foods:
	print("My favorite pizzas are:" + my_food.title())
for your_food in your_foods:
	print("your favorite pizzas are:" + your_food.title())
 




 
