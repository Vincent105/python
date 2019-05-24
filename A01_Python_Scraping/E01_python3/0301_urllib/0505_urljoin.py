from urllib.parse import urljoin

print(urljoin('http://wwww.baidu.com', 'FAQ.html'))                       
print(urljoin('http://wwww.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://wwww.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://wwww.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://wwww.baidu.com', '?category=2#comment'))                       

