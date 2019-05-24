import http.cookiejar, urllib.request

'''取得cookies'''
cookie = http.cookiejar.CookieJar()
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name + '=' + item.value)

'''cookies寫出文字檔 - Mozilla格式'''
filename = 'A01_Python_Scraping\\E01_python3\\0301_basic_urllib\\cookies1.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('http://www.baidu.com')    
cookie.save(ignore_discard=True, ignore_expires=True)

'''cookies寫出文字檔 - LWP格式'''
filename = 'A01_Python_Scraping\\E01_python3\\0301_basic_urllib\\cookies2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('http://www.baidu.com')    
cookie.save(ignore_discard=True, ignore_expires=True)

'''透過讀取cookies，進行請求'''
cookie = http.cookiejar.LWPCookieJar()
cookie.load('A01_Python_Scraping\\E01_python3\\0301_basic_urllib\\cookies2.txt',ignore_discard=True, ignore_expires=True)
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('http://www.baidu.com')    
print(response.read().decode('utf-8'))