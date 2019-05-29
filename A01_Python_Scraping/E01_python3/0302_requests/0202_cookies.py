import requests

r = requests.get('http://www.baidu.com')
print(r.cookies)

for key, value in r.cookies.items():
    print(key,value)

#利用cookies模擬登錄
headers = {
    'cookie': '_zap=2504a4f7-c072-4509-9515-f13c63e86447; d_c0="AGBmn3VMLg-PTm9USIYZL6Fgh-0Xlyh5X1c=|1553585088"; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; _xsrf=Y1aSjQivJhdjJaZY3uUK17LKhIsu2q4r; capsion_ticket="2|1:0|10:1559111896|14:capsion_ticket|44:ZTAwYzI4OTMyOGFhNGEwZmJhZjk5N2E5Nzc3MDFjMTc=|01fae3e059610d5ba1cae8bcbb764eb2af13232b164ff89baaa827520fb731ec"; z_c0="2|1:0|10:1559111936|4:z_c0|92:Mi4xRWhuMkR3QUFBQUFBWUdhZmRVd3VEeVlBQUFCZ0FsVk5BSGZiWFFDUThYeFlkNEdMbGlqZVBUREdadjlxQ001S2x3|d10539146e63c56c7eb9a94d031c65f00641c487c3d4c76d3985e60867af8f14"; tst=r',
    'Host': 'www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }    
r = requests.get('http://www.zhihu.com',headers=headers)
print(r.text)

#利用session維持，以下是不同session
requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

#利用session維持，以下是相同session
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
