import requests

files = {
    'file': open('A01_Python_Scraping\\E01_python3\\0302_requests\\favicon.ico','rb')
    }

r = requests.post("http://httpbin.org/post", files=files)    
print(r.text)




