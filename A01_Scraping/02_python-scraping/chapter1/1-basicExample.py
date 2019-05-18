from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except URLError as e:
    print(e)    
except HTTPError as g:
    print(g)    
else:
    bsObj = BeautifulSoup(html.read(),"html.parser")
    print(bsObj.html)
    print('\n')
    print(bsObj.body.h1)
    print(bsObj.html.body.h1)
    print(bsObj.h1)
    print(bsObj.title)
    




