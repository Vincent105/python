from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://www.baidu.com')
soup = BeautifulSoup(response.read(), "html.parser")
print(soup.title)
 