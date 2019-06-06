#解壓可迭代對象賦值給多個變量
#Case 1 
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, mail, *phone_numbers = record
print(name)
print(phone_numbers)                #解壓出的*變量永遠都是列表類型，不管解壓的電話號碼數量是多少（包括 0 個）。

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

#迭代解壓語法是專門為解壓不確定個數或任意個數元素的可迭代對象而設計的。 通常，這些可迭代對象的元素結構有確定的規則
# 星號表達式讓開發人員可以很容易的利用這些規則來解壓出元素來。 而不是通過一些比較複雜的手段去獲取這些關聯的元素值。

#星號表達式在迭代元素為可變長元組的序列時是很有用的。 下面是一個帶有標籤的元組序列：

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

#字符串的分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

#解壓元素後丟棄，可以廢棄名稱，比如 _。
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

items = [1, 10, 7, 4, 5, 9]
head, *item = items
print(head)
print(item)




