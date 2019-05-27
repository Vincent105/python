from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

url = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(url.read(),'lxml')

'''
Note that this returns only the first instance of the h1 tag found on the page.
should be aware that this will retrieve the first instance of the tag only,
 and not necessarily the one that you’re looking for.
'''
print(bs.head)
print(bs.title)
print(bs.body)
print(bs.h1)
print(bs.div)

try:
    badContent = bs.h1
except AttributeError as e:    
    print("Tag  was not found")
else:
    if badContent == None:
        print("Tag  was not found")    
    else:
        print(badContent)        