import re 

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventure of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')   
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
