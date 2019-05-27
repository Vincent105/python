# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'lxml')

#return both the green and organ span tags in the HTML document:
namelist = bs.findAll('span',{'class':{'green','organ'}})         #findAll(tagName, tagAttributes)
for name in namelist:
    print(name.get_text())                              #separate the content from the tags.