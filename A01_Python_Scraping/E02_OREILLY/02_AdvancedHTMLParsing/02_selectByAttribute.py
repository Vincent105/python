from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'lxml')

#returns a list of all the header tags in a document
namelist = bs.findAll({'h1','h2','h3','h4','h5','h6'})         
for name in namelist:
    print(name.get_text())            

#find is equivalent to the same find_all call, with a limit of 1.
namelist = bs.find_all(text='the prince',limit=3)
print(namelist)

#keyword
namelist = bs.find_all(id='text')
print(namelist)

namelist = bs.find_all(id='text')
print(namelist[0].get_text())

namelist = bs.find_all('',{'id':'text'})
print(namelist[0].get_text())

#keyword class_ & class
namelist = bs.find_all(class_='green')
print(namelist[0].get_text())

namelist = bs.find_all('',{'class':'green'})
print(namelist[0].get_text())