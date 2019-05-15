import re

xmasRegex = re.compile(r'\d+\s\w+')
m = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
    swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')    

print(m)    

#自定義字符分類
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#範圍表示
vowelRegex = re.compile(r'[a-eA-E0-9.]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#集合反向匹配!!
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#用插入符號表示必須存在於開頭
beginWithHello = re.compile(r'^Hello')
print(beginWithHello.search('Hello World'))
print(beginWithHello.search('She say Hello.'))

#$表示字串必須以此正則式結束
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty-two.'))

#^\d+$表示字串必須從開始到結束都是數字
wholeWithNumber = re.compile(r'^\d+$')
print(wholeWithNumber.search('123145'))
print(wholeWithNumber.search('123xyz3145'))









