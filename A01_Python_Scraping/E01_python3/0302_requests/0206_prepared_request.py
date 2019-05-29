from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}    
s = Session()
req = Request('POST',url,data=data,headers=headers)             #建構要求對象
preped = s.prepare_request(req)                                 #用session的prepare_request轉換
r = s.send(preped)                                              #在同一個session進行發送    
print(r.text)


