#如果结果为0（意味着current_number 可被2整除），就执行continue 语句，[让Python忽略余下的代码，并返回
#到循环的开头。] 如果当前的数字不能被2整除，就执行循环中余下的代码， Python将这个数字打印出来：

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number) 