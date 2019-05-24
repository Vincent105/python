from urllib.parse import unquote

#透過方法將中文字轉換為url編碼
url = 'http://www.baidu.com/s?wd=%E8%82%A1%E7%A5%A8'
print(unquote(url))