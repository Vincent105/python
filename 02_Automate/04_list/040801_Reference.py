#變量
spam = 42
cheese = spam
spam = 100

print(cheese)
print(spam)

#当你将列表赋给一个变量时，实际上是将列表的“引用”
#赋给了该变量。引用是一个值，指向某些数据。列表引用是指向一个列表的值。
#在变量必须保存可变数据类型的值时，例如列表或字典，Python 就使用引用。
#对于不可变的数据类型的值， 例如字符串、 整型或元组， Python变量就保存值本身

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'

print(cheese)
print(spam)

def eggs(somePara):
	somePara.append('Hello')

spam = [1,2,3]
eggs(spam)

print(spam)