import re

haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

mo3 = haRegex.search('HaHa')
print(mo3==None)

mo4 = haRegex.search('HaHaHaHaHa')
print(mo4.group())

mo5 = haRegex.search('HaHaHaHaHaHa')
print(mo5.group())