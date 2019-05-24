import requests

request = requests.get('https://www.baidu.com')
print(type(request))
print(request.status_code)
print(type(request.text))
print(request.text)
print(request.cookies)

data = {
    'name': 'germey',
    'age': 22
}

request = requests.get('http://httpbin.org/get', params=data)
print(type(request.text))
print(request.text)
print(request.json())           #可以將json格式的字串轉為字典
