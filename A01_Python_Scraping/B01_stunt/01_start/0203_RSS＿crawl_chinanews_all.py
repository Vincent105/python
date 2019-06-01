from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import json
import time
from urllib import error

'''未能完善基本模組。擷取時會遇到http404 error'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

#取得所有連結
resource = urlopen('http://www.chinanews.com/rss/rss_2.html')
rss_page = BeautifulSoup(resource.read(), 'lxml')
rss_links = set([item['href'] for item in rss_page.find_all('a')])

def crawl_feed(url):
    res = Request(url,headers=headers)
    response = urlopen(res,timeout=10)
    rss = BeautifulSoup(response.read(), 'lxml')
    items = []
    print("Crawling %s" % url)

    for item in rss.find_all('item'):
        try:
            feed_item = {
                'title': item.title.text,
                'link': item.contents[2],
                'description': item.description.text,
                'pubDate': u'' if item.pubDate is None else item.pubDate.text
            }
            items.append(feed_item)
        except Exception as e:
            print("Crawling%s error:" % url)       
        except error.HTTPError as e:
            continue   
        except:
            continue                       
    time.sleep(2)               
    return items

feed_items = []

for link in rss_links:
    feed_items += crawl_feed(link)

with open("A01_Python_Scraping\\B01_stunt\\01_start\\result_all.json",'wt') as file:
    file.write(json.dumps(feed_items))

print('Total crawl %s items'%len(feed_items))

