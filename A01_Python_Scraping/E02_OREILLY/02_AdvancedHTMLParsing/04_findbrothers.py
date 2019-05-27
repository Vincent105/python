from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html,'html.parser')
'''The output of this code is to print all rows of products from the product table,
except for the first title row. Objects cannot be siblings with themselves.'''

for sobling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sobling)
print(bsObj.find('table',{'id':'giftList'}).tr)


