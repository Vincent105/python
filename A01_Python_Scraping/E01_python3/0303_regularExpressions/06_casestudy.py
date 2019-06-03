import re
import requests


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    print(items)


html = main()
