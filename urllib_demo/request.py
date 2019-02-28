import urllib.request
import http.cookiejar


def save_cookie():
    filename = 'cookies.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + '=' + item.value)

    cookie.save(ignore_discard=True, ignore_expires=True)


def load_cookie():
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf8'))



save_cookie()
# load_cookie()
