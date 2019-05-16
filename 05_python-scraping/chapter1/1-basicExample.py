from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


try:
    html = urlopen("http://pythonscraping.com/pages/page1.htm")
except urllib.error.URLError as e:
    print(e)    
except urllib.error.HTTPError as g:
    print(g)        
else:
    bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.html)
print('\n')
print(bsObj.html.body)
print(bsObj.html.body.h1)
print(bsObj.h1)
print(bsObj.title)




