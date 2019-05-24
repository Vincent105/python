from urllib.parse import urlparse

#urllib .parse.urlparse(urlstring, scheme'', allow_fragments=True)
result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='http', allow_fragments=False)
print(type(result), result)

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result, result[0], result[1], result[2],result.netloc,sep='\n')
