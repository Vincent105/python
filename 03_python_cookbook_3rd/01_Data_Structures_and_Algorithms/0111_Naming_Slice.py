# 命名切片 避免hardcode相關切片
record = '....................100 .......513.25 ..........'

cost = int(record[20:23]) * float(record[31:37])
print(cost)

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0, 1, 2, 3, 4, 5, 6]
a_cut = slice(2, 4)
print(items[2:4])
print(items[a_cut])

del items[a_cut]
print(items)

# a.start , a.stop , a.step 屬性
a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))): 
    print(s[i])

for i in range(*(5,10,2)):  #透過*號將參數解出
    print(i)

for i in range(*[5,10,2]):  #透過*號將參數解出 
    print(i)
