import re 
import requests

hearders = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
'''
r = requests.get("https://www.zhihu.com/explore", headers=hearders)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
'''
r2 = requests.get("https://github.com/favicon.ico", headers=hearders)
#print(r2.text)                 #byte轉換為str，所以會產生亂碼        
print(r2.content)               #byte類型
with open('A01_Python_Scraping\\E01_python3\\0302_requests\\favicon.ico','wb') as f:
    f.write(r2.content)