import re 

#用*匹配0次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventure of Batman.')
print(mo1.group())

mo2 = batRegex.search('The adventure of Batwoman.')
print(mo2.group())

mo3 = batRegex.search('The adventure of Batwowoman.')
print(mo3.group())