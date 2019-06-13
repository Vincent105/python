from bs4 import BeautifulSoup

html = '''
<html> <head ><title>The Dormouse's story</title></head>
<body >
<p class="title" name="dromouse">< b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class= "sister" id="linkl">< ! - Elsie … >< la>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> ;
and they lived at the bottom of a well . </p>
<p class="story"> 
'''
soup = BeautifulSoup(html,"lxml")
print(soup.prettify())
print("測試取得標題文字",soup.title.string)
