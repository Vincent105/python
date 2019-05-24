import urllib.request
import urllib.parse
#設置超時時間控制，引用下列第三方套件
import socket   
import urllib.error

#urlopen() urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
response = urllib.request.urlopen('http://www.python.org')
print(type(response))
print(response.read().decode('UTF-8'))                  #調用方法取得返回的網頁內容
print(response.status)                                  #調用屬性取得返回的網頁狀態
print(response.getheaders())                            #調用方法取得所有的網頁表頭            
print(response.getheader('Server'))                     #調用方法傳遞單參數取得表頭
print('\n')

#urlopen() data參數
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)          #透過測試post請求網站，傳遞form請求檔
print(response.read())

#urlopen() timepout參數
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.0001) #透過測試get請求網站，    
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
