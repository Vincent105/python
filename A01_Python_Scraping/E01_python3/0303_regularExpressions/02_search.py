'''
match()，只能夠從開頭處開始進行比對，只適合檢查某個字串是否符合正規表示式
search()，比對時掃描整個字串，返回第一個成功結果
'''
import re

content = 'Extra stings Hello 1234567 World This is a Regex Demo Extra stings '
result = re.match('Hello.*(\d+).*?Demo', content)
print(result)

content = 'Extra stings Hello 1234567 World This is a Regex Demo Extra stings '
result = re.search('Hello.*(\d+).*?Demo', content)
print(result)

filename = 'A01_Python_Scraping\\E01_python3\\0303_regularExpressions\\test.html'
with open(filename, encoding="utf-8") as fileobject:
    contents = fileobject.read()

print(contents)

result = re.search('<li.*active.*?singer="(.*?)">(.*?)</a>', contents, re.S)
if result:
    print(result.group(1), result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', contents, re.S)
if result:
    print(result.group(1), result.group(2))

result = re.search('<li.*?singer="(.*?)">(.*?)</a>', contents)
if result:
    print(result.group(1), result.group(2))