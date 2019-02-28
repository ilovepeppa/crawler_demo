from urllib.parse import urlparse, urlunparse, \
    urlsplit, urlunsplit, urljoin, \
    urlencode, parse_qs, parse_qsl, \
    quote, unquote

url = 'http://www.baidu.com/index.html;user?id=5#comment'

result = urlparse(url)
print(type(result), result, sep='\n')

data = ['http', 'www.baidu.com', 'index.html', '', 'a=6', 'comment']
print(urlunparse(data))

result = urlsplit(url)
print(type(result), result, sep='\n')

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

params = {
    'name': 'lance',
    'age': 24
}
url = 'http://www.baidu.com?' + urlencode(params)
print(url)

query = 'name=lance&age=22'
print(parse_qs(query))
print(parse_qsl(query))

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)


url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

