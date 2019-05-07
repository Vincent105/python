names = ['admin','Vincent','Esther','John','Andy']

if names:
	for name in names:
		if name.lower() == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + name.title() + " thank for your logging in again.")	
else:
	print("We have to find some users.")	

current_users = ['John','b','c','d','e']
new_users = ['JOHN','b','f','g','h']

for new_user in new_users:
	if new_user.lower() in current_users:	
		print(new_user + " 輸入名稱已被使用,請命名新帳號:")
	elif new_user.upper() in current_users:	
		print(new_user + " 輸入名稱已被使用,請命名新帳號:")		
	elif new_user.title() in current_users:	
		print(new_user + " 輸入名稱已被使用,請命名新帳號:")				
	else:
		print(new_user + " 姓名尚未被使用")	

numbers = ['1','2','3','4','5','6','7','8','9']

for number in numbers:
	if number == '1':
		print("1st")
	elif number == '2':
		print("2nd")
	elif number == '3':
		print("3rd")		
	elif number == '4':
		print("4th")		
	elif number == '5':
		print("5th")		
	else:
		print("Unknow")	
