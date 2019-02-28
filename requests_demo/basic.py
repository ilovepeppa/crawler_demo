import requests
import re


def a():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }

    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)


def b():
    r = requests.get('https://github.com/favicon.ico')
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)


def c():
    r = requests.post('http://httpbin.org/post', data={
        'name': 'lance',
        'age': 24
    })
    print(r.text)


b()