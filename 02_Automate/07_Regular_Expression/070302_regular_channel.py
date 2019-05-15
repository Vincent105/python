import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

#第一次出現的match將進行返回
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

mo2 = heroRegex.findall('Tina Fey and Batman')
a, b = mo2
print(a)
print(b)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

