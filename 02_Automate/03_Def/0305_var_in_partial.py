#局部作用域不能使用其他局部作用域内的变量
def spam():
	eggs = 99
	bacon()
	print(bacon())
	print(eggs)

def bacon():
	ham = 101
	eggs = 0

spam()

#全局变量可以在局部作用域中读取
def spam():
	print(eggs)
eggs = 42
spam()
print(eggs)

