from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except URLError as error_1:
        return None
    except HTTPError as error_2:
        return None
    try:        
        bsObj = BeautifulSoup(html.read(),"html.parser")         
        title = bsObj.html.h1
    except AttributeError as error_3:
        return None        
    return title    

title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if title == None:
    print("Title counld not find.")
else:
    print(title)    
