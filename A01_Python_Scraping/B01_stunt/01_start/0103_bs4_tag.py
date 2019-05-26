from bs4 import BeautifulSoup

html = BeautifulSoup("<h1>test</h1>", "html.parser")
print(html.h1)

soup = BeautifulSoup("<b class=boldest>粗體</b>","html.parser")
tag = soup.b

print(tag) 
print(type(tag))
print(tag['class'])

print(tag.attrs)            #透過attrs屬性取得xml,html屬性