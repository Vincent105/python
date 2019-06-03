import re
'''透過sub簡化正則式的複雜度'''
content = '54aKS4yrsoiRS4ixSL2g'
content = re.sub('\d+', '', content)

print(content)

filename = 'A01_Python_Scraping\\E01_python3\\0303_regularExpressions\\test.html'
with open(filename, encoding="utf-8") as fileobject:
    contents = fileobject.read()

'''    
print(contents)

results = re.findall(
    '<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', contents, re.S)

for result in results:
    print(result[1])
'''
contents = re.sub('<a.*?>|</a>', '', contents)
print(contents)

results = re.findall('<li.*?>(.*?)</li>', contents, re.S)
for result in results:
    print(result.strip())
