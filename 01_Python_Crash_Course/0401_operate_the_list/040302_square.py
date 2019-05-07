#使用臨時變量，計算平方
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)

#省略臨時變量，計算平方
squares2 = []
for value in range(1,11):
	squares2.append(value ** 2)
print(squares2)	
