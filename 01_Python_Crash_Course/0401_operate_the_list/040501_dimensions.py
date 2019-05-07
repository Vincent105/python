#使用圆括号而不是方括号来标识，。
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#试图修改元组的操作是被禁止的，
#dimensions[0] = 250

#使用for循环来遍历元组中的所有值：
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)

#虽然不能修改元组的元素，但可以给存储元组的变量赋值。可重新定義整個元組
dimensions = (200,500)	
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,300,700)	
print("New dimensions:")		
for dimension in dimensions:
	print("New number is " + str(dimension))








