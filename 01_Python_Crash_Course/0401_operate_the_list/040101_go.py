# for循環，從列表magicians中取出一个名字，并将其存储在變數magician。
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

# for循環，每個縮排的代碼行都是循環的一部份，且將針對列表中每個數值都執行一次。
for magician in magicians:			#for循環後需要冒號：
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next tricks," + magician.title() + ".\n")

# for循環,沒有縮排的代碼行只執行一次，而不會重複進行。
print("Thank you everyone!")


