from urllib.parse import quote

#透過方法將中文字轉換為url編碼
keyword = '股票'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url)