'''若網頁開啟時提示輸入框_可透過範例處理帳號密碼驗證'''
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost',auth=HTTPBasicAuth('username','password'))
print(r.status_code)


#request也支援OAuth認證，不過要另外安裝oauth第三方套件
