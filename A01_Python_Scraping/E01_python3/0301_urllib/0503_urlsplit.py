from urllib.parse import urlsplit

#與urlparse類式，但不解析params
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result, result.netloc, result[1])
