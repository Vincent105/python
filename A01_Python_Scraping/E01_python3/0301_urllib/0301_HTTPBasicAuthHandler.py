'''若網頁開啟時提示輸入框_可透過範例處理帳號密碼驗證'''
from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener
from urllib.error import URLError
import ssl

username = '帳號'
password = '密碼'    
url = 'https://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url , username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

#解決[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)
ssl._create_default_https_context = ssl._create_unverified_context

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)    