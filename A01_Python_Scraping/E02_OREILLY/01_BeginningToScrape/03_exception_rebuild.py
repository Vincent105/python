from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        urlTarget = urlopen(url)
    except HTTPError as e:    
        return None
    try:   
        bs = BeautifulSoup(urlTarget.read(),'lxml')
        title = bs.body.h1
    except AttributeError as e:    
        return None
    return title

try_path = getTitle('http://www.pythonscraping.com/pages/page1.html')
if try_path == None:
    print('Title could not founded')
else:
    print(try_path)    