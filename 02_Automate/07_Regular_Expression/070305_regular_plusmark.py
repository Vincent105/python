import re
#用+匹配1次或多次
batRegex = re.compile(r'Bat(wo)+man')               #+代表wo至少需要匹配一次
mo1 = batRegex.search('The adventure of Batman.')
print(mo1 == None)

mo2 = batRegex.search('The adventure of Batwoman.')
print(mo2.group())

mo3 = batRegex.search('The adventure of Batwowoman.')
print(mo3.group())