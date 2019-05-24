import requests

data = {
    'name': 'germey',
    'age': 22
    }

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
print(r.content)

r2 = requests.post('https://www.jianshu.com', headers=headers)
print(r2.status_code)
print(r2.headers)
print(r2.cookies)
print(r2.url)
print(r2.history)

r3 = requests.post('https://www.jianshu.com', headers=headers)
exit() if not r3.status_code == requests.codes['not_found'] else print('Request successfully')

response1 = requests.get("https://fanyi.baidu.com") 
print(response1.cookies)
for key, value in response1.cookies.items():
    print(key + ':' +value)

