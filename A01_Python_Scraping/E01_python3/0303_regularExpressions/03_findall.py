import re
#如果只是获取第一个内容，可以用 search （）方法 。 当需要提取多个内容时，可以用于indall()方法。

filename = 'A01_Python_Scraping\\E01_python3\\0303_regularExpressions\\test.html'
with open(filename, encoding="utf-8") as fileobject:
    contents = fileobject.read()

results = re.findall('<li.*?singer="(.*?)">(.*?)</a>', contents, re.S)
print(results)
for result in results:
    print(result[0],result[1])

