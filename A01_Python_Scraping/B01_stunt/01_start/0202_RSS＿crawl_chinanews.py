from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

response = urlopen("http://www.chinanews.com/rss/scroll-news.xml")
rss = BeautifulSoup(response.read(), "xml")
print(rss)

items = []

for item in rss.findAll("item"):

    feed_item = {
        'title': item.title.text,
        'link': item.link.text,
        'description': item.description.text,
        'pubDate': item.pubDate.text
    }

    items.append(feed_item)

for item in items:
    for attr, value in item.items():
        print(attr + ':' + value)
    print('\n')

with open("A01_Python_Scraping\\B01_stunt\\01_start\\result.json",
          'wt') as file:
    file.write(json.dumps(items))