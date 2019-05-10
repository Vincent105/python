#任何序列（或者是可迭代對象）可以賦值語句解壓並賦值給多個變量。 唯一的前提就是變量的數量必須跟序列元素的數量是一樣的。
#CASE 1
p = (4, 5)
x, y = p

print(x)
print(y)

#CASE 2
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, share, price, date = data
print(name)
print(date)

#CASE 3 
name, share, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)

#CASE 4 包括字符串，文件對象，迭代器和生成器。
s = 'Hello'
a, b, c, d, e = s
print(a)

#CASE 5 只想解壓一部分，丟棄其他的值。這種情況 Python 並沒有提供特殊的語法。 可以使用任意變量名去佔位，到時候丟掉這些變量。
#但必須保證 所選用的佔位變量名在其他地方沒被使用到。
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, share, price, _ = data
print(share)