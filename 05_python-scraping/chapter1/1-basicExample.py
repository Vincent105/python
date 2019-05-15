from urllib.request import urlopen
from bs4 import BeautifulSoup

#pip install beautifulsoup4 

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())




