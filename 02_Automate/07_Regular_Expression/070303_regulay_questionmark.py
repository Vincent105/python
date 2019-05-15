import re 

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventure of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group())