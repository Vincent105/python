#4-3 重0數到20
digits_2 = []
for value in range(1,21):
	value_t = value
	digits_2.append(value_t)
print(digits_2)

digits_1 = []
for value in range(1,21):
	digits_1.append(value)
print(digits_1)	

digits = [value for value in range(1,21)]
print(digits)

#4-4 到1萬 求最大 最小 及 總和
digits_100 = [value for value in range(1,10001)]
print(digits_100)
print(min(digits_100))
print(max(digits_100))
print(sum(digits_100))

#4-6 奇數
numbers =[]
for value in range(1,21,2):
	numbers.append(value)
print(numbers)	

#4-7 3的倍數
numbers =[]
for value in range(3,31,3):
	numbers.append(value)
print(numbers)	

#4-8 立方
numbers33 = []
for value in range(1,11):
	numbers33.append(value ** 3)
print(numbers33)	

#4-9 立方解析
numbers3 =[value ** 3 for value in range(1,11)]
print(numbers3)	



