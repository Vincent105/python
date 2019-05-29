import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }    

proxies = {
    'http': 'http://192.236.160.50:3128',                   #替換代理伺服器位置
    'https': 'https://45.76.170.103:3128',                   #替換代理伺服器位置    
}

requests.get('https://www.taobao.com',proxies=proxies,headers=headers,timeout=20)

#可分別指定連接,讀取,總和秒數
# requests.get('https://www.taobao.com',proxies=proxies,headers=headers,timeout=(9, 11, 20))


#request也支援socks協議的代理，不過要另外安裝socks第三方套件