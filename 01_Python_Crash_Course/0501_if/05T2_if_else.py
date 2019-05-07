alien_colors = ['green','red','yellow']
user1_color = 'purple' 
user2_color = 'green' 

if user1_color in alien_colors:
	print("Player,Your have get 5 points.")

if user2_color in alien_colors:
	print("Player,Your have get 5 points.")	

if user1_color == 'green':
	print("Player,Your have get 5 points.")		

if user2_color == 'green':
	print("Player,Your have get 10 points.")		

if 	user1_color == 'green':
	print("Player,Your have get 5 points.")		
else: 	
	print("Player,Your have get 0 points.")		

if 	user2_color == 'green':
	print("Player,Your have get 10 points.")		
else: 	
	print("Player,Your have get 0 points.")			

user3_color ='red'
user4_color ='yellow'
user5_color ='green'

if 	user3_color == 'green':
	print("Player,Your have get 5 points.")			
elif user3_color == 'red':
	print("Player,Your have get 10 points.")			
else:
	print("Player,Your have get 15 points.")			

if 	user4_color == 'green':
	print("Player,Your have get 5 points.")			
elif user4_color == 'red':
	print("Player,Your have get 10 points.")			
else:
	print("Player,Your have get 15 points.")			

if 	user5_color == 'green':
	print("Player,Your have get 5 points.")			
elif user5_color == 'red':
	print("Player,Your have get 10 points.")			
else:
	print("Player,Your have get 15 points.")			

age = 4
if age < 2:
	print("目前是個嬰兒")
elif age >= 2 and age < 4:
	print("正在學習走路")
elif age >= 4 and age < 13:
	print("目前是個兒童")
elif age >= 13 and age > 20:
	print("目前是青少年")
elif age >= 20 and age > 65:
	print("目前是成人年")	
else:
	print("目前是老年人")			







