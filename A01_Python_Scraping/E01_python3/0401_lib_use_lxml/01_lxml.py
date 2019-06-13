'''
@   選取屬性
..  選擇當前節點的父節點
.   選擇當前節點
/   從當前節點選擇直接子節點
//  從當前節點選取子孫節點
'''

from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>              
</ul>
</div>
'''

html = etree.HTML(text)
result = etree.tostring(html)  # etree可自動修正html文本，補足</li>
print(result.decode('UTF-8'))

# 讀取本機檔案
html_2 = etree.parse(
    'A01_Python_Scraping\\E01_python3\\0401_lib_use_lxml\\test.html', etree.HTMLParser())
result_2 = etree.tostring(html_2)
print(result_2.decode('UTF-8'))

# 讀取XPath所有節點
html_3 = etree.parse(
    'A01_Python_Scraping\\E01_python3\\0401_lib_use_lxml\\test.html', etree.HTMLParser())

result_3a = html_3.xpath('//*')
for item in result_3a:
    print("讀取XPath所有節點", item)

# 讀取XPath<li>節點
result_3b = html_3.xpath('//li')
for item in result_3b:
    print("讀取XPath<li>節點", item)

# 讀取XPath子節點
result_3c = html_3.xpath('//li/a/text()')
for item in result_3c:
    print("讀取XPath子節點", item)

# 讀取XPath所有子孫節點
result_3d = html_3.xpath('//ul//a/text()')
for item in result_3d:
    print("讀取XPath所有子孫節點", item)

result_3e = html_3.xpath('//ul/a')  # 無法取得，因為ul下並沒有a的子節點，只有li子節點。
for item in result_3e:
    print("讀取XPath所有子孫節點", item)

# 讀取XPath父節點
result_3f = html_3.xpath('//a[@href="link4.html"]/../@class')
print("讀取XPath父節點方式一:", result_3f)

result_3g = html_3.xpath(
    '//a[@href="link4.html"]/parent::*/@class')  # 可以透過parent::*取得父節點
print("讀取XPath父節點方式二:", result_3g)

# 進行屬性匹配
result_3h = html_3.xpath('//li[@class="item-0"]/a/text()')
print("進行屬性匹配:", result_3h)

result_3h = html_3.xpath('//li[@class="item-0"]//text()')
print("進行屬性匹配(子孫節點可能取得換行符號):", result_3h)

# 節點屬性獲取
# 屬性匹配是中括弧加屬性名與值來限定某個屬性，如［＠href="linkl.html”］，而此處的＠href指的是獲取節點的某個屬性
result_3i = html_3.xpath('//li/a/@href')
print("節點屬性獲取:", result_3i)

# 屬性匹配--多值

text = '''
<li class="li li-first" name="item"><a href＝"link.html">first item_1</a><lli>
<li class="item-0"><a href="link1.html">first item_2</a></li>
'''
html_New = etree.HTML(text)
result = html_New.xpath('//li[@class="li"]/a//text()')
print(result)

result = html_New.xpath('//li[@class="li li-first"]/a//text()')
print(result)

result = html_New.xpath('//li[contains(@class,"item-0")]/a/text()')
print(result)

# 屬性匹配--多值 and
result = html_New.xpath(
    '//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)

# 按期望的序列進行選擇
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>              
</ul>
</div>
'''

html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[2]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)

# 按Xpath軸進行選擇
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')  # 選取當前節點的所有屬性。
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')   
print(result)
result = html.xpath('//li[1]/descendant::span')   
print(result)
result = html.xpath('//li[1]/following::*[2]')   
print(result)
result = html.xpath('//li[1]/following::*[2]')   
print(result)