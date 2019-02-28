import requests
import requests.cookies


def a():
    files = {
        'file': open('favicon.ico', 'rb')
    }
    r = requests.post('http://httpbin.org/post', files=files)
    print(r.text)


def b():
    r = requests.get('https://www.baidu.com', headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    })
    print(r.cookies)
    for key, value in r.cookies.items():
        print(key + '=' + value)


def c():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Cookie': '_zap=a0bc39a5-3fcb-4cea-b90f-feb423f99807; d_c0="AFAhEtSYxw6PTrApweLqfYPHjVm5_MGhrJE=|1546692895"; z_c0="2|1:0|10:1546776788|4:z_c0|92:Mi4xY1JUdUJnQUFBQUFBVUNFUzFKakhEaVlBQUFCZ0FsVk4xRDRmWFFCR2FIcnYtMXpjRktkVnVVV1dxejJqQVI4c0F3|cf2258082c10e93a1f31991deb020e96f623d40aad6287dc1d9b2fc85803fcda"; tst=r; _xsrf=1YNlJuRpxd9xvXD9c25KNskTUzbSsnxW; q_c1=491ee5da8ac3432ba712e1cb658cf42b|1549865260000|1546692897000; __utma=51854390.530225059.1551234814.1551234814.1551234814.1; __utmb=51854390.0.10.1551234814; __utmc=51854390; __utmz=51854390.1551234814.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20171217=1^3=entry_date=20171217=1; tgw_l7_route=060f637cd101836814f6c53316f73463',
        'Host': 'www.zhihu.com'
    }
    r = requests.get('https://www.zhihu.com', headers=headers)
    print(r.text)


def d():
    cookies = '_zap=a0bc39a5-3fcb-4cea-b90f-feb423f99807; d_c0="AFAhEtSYxw6PTrApweLqfYPHjVm5_MGhrJE=|1546692895"; z_c0="2|1:0|10:1546776788|4:z_c0|92:Mi4xY1JUdUJnQUFBQUFBVUNFUzFKakhEaVlBQUFCZ0FsVk4xRDRmWFFCR2FIcnYtMXpjRktkVnVVV1dxejJqQVI4c0F3|cf2258082c10e93a1f31991deb020e96f623d40aad6287dc1d9b2fc85803fcda"; tst=r; _xsrf=1YNlJuRpxd9xvXD9c25KNskTUzbSsnxW; q_c1=491ee5da8ac3432ba712e1cb658cf42b|1549865260000|1546692897000; __utma=51854390.530225059.1551234814.1551234814.1551234814.1; __utmb=51854390.0.10.1551234814; __utmc=51854390; __utmz=51854390.1551234814.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20171217=1^3=entry_date=20171217=1; tgw_l7_route=060f637cd101836814f6c53316f73463'
    jar = requests.cookies.RequestsCookieJar()
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    for cookie in cookies.split(';'):
        key, val = cookie.split('=', 1)
        jar.set(key, val)

    r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
    print(r.text)


def e():
    session = requests.Session()
    session.get('http://httpbin.org/cookies/set/number/123456789')
    r = session.get('http://httpbin.org/cookies')
    print(r.text)


def f():
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }
    requests.get('https://www.taobao.com', proxies=proxies)


def g():
    r = requests.get('http://localhost:5000', auth=('username', 'password'))
    print(r.status_code)


def h():
    url = 'http://httpbin.org/post'
    data = {
        'name': 'lance'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    s = requests.Session()
    req = requests.Request('POST', url, data=data, headers=headers)
    prepared = s.prepare_request(req)
    r = s.send(prepared)
    print(r.text)
