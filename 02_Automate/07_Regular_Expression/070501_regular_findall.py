import re 
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Cell:415-555-9999, Work:415-555-1111')    
print(mo.group())

mof = phoneNumberRegex.findall('Cell:415-555-9999, Work:415-555-1111')
number1, number2 = mof
print(number1)
print(number2)

'''
1．如果调用在一个没有分组的正则表达式上， 例如\d\d\d-\d\d\d-\d\d\d\d， 方法findall()将返回一个匹配字符串的列表。
2． 如果调用在一个有分组的正则表达式上， 例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)， 方法 findall()将返回一个字符串的元组的列表（每个分组对应一个字符串）
'''
