from bs4 import BeautifulSoup
'''從html解析tag'''

html = BeautifulSoup(open("A01_Python_Scraping\\B01_stunt\\01_start\index.html",encoding = 'utf8').read(),"lxml")
products = []

for ele in html.select("article"):
    _name = ele.header.text
    _color = (ele.select_one('p.color > span:nth-of-type(2)').text)
    _value = int(ele.select_one('p.price > span:nth-of-type(2)').text)  #指定每个span元素匹配同类型中的第2个同级兄弟
    products.append((_name,_color,_value))
print(products)
for name, color, price in products:
    print(name + ':' + str(price) + color)