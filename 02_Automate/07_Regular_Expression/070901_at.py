import re 

#使用通配字符
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

#使用通配字符搭配星號取得所有字符
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))


