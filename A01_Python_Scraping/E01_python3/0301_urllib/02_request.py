from urllib import request, parse

#Request urllib.request.Request (url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
url = 'http://www.python.org/post'
hearders = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Host': 'httpbin.org',
}

dict ={
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict),encoding='utf-8')

req = request.Request(url=url, data=data, headers=hearders,method='POST')     #建構Post請求
req.add_header("Origin","http://httpbin.org")                                 #透過add_header()方法添加表頭

response = request.urlopen(req)                                               
print(response.read().decode('utf-8'))