from urllib.parse import urlencode

params = {
    'name': 'Gemery',
    'age': '22'
}

base_url = 'www.baidu.com?'
url = base_url + urlencode(params)
print(url)
