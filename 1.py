from grab import Grab as gr
from pyquery import PyQuery as pq

url = 'https://www.yahoo.com'

g = gr()
resp = g.go(url,encoding='utf-8')

doc = pq(resp.body)
span = doc('.drag-item.D-b.Td-n').find("span") 

print('取得所有頻道:')
for item in span.items():
    print(item.text())
    