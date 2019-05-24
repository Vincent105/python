from urllib.error import URLError
from urllib.request import build_opener, ProxyHandler

proxy_handler = ProxyHandler({
    'http': 'http://134.209.79.112:3128',                   #替換代理伺服器位置
    'https': 'https://35.199.91.20:3128',                   #替換代理伺服器位置
})

opener = build_opener(proxy_handler)

try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)    