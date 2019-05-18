import requests
from bs4 import BeautifulSoup

link = 'http://www.santostang.com'
headers ={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 \
        (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'}
r = requests.get(link, headers=headers)         

#print(r.text)

soup = BeautifulSoup(r.text,"lxml")         #取得字串本體
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)
print(r.encoding)               #取得網頁編碼
print(r.status_code)            #取得回應狀態   200：請求成功 4xx:客戶端錯誤 5xx：伺服器端錯誤
print(r.json) 

with open('A01_Scraping\\01_santostang\\title.txt','w',encoding="utf-8") as f:
    f.write(title)
    f.close()
    