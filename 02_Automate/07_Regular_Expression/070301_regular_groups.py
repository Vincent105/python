import re 

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('test number is 123-456-7890')     
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

areaCode, mainNumber = mo.groups()      #groups返回多組元組，可運用複數解壓進行賦值。
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')        #用\( \) 解決group 分組問題。
mo = phoneNumRegex.search('test number is (123)456-7890')
print(mo.group(1))
print(mo.group(2))



