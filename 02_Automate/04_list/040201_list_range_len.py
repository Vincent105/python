for i in range(4):
	print(i)

for i in [0,1,2,3]:	
	print(i)

#常见Python技巧,在 for 循环中使用 range(len(someList))，迭代列表的每一个下标
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
	print('Index ' + str(i) + ' is ' + supplies[i])


