from bs4 import BeautifulSoup
'''從html解析tag'''

html = BeautifulSoup(open("A01_Python_Scraping\\B01_stunt\\01_start\index.html",encoding = 'utf8').read(),"lxml")
print(html.title)

html = BeautifulSoup(open("A01_Python_Scraping\\B01_stunt\\01_start\index.html",encoding = 'utf8').read(),"html.parser")
print(html.title)

products = []

for ele in html.find_all("article"):
    _name = ele.header.text
    _color = ele.find("p",class_='color').find('span').find_next('span').text
    _value = int(ele.find("p",class_='price').find('span').find_next("span").text)
    products.append((_name,_color,_value))
print(products)
for name, color, price in products:
    print(name + ':' + str(price) + color)