import json
import requests
from bs4 import BeautifulSoup


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    films = soup.select('.board-wrapper dd')
    for film in films:
        item = {}
        item['index'] = film.select('.board-index')[0].string
        item['image'] = film.select('.board-img')[0]['data-src']
        item['title'] = film.select('.name a[data-val]')[0].string
        item['author'] = film.select('.star')[0].string.strip()[3:].split(',')
        item['time'] = film.select('.releasetime')[0].string[5:]
        item['score'] = ''.join([x.string for x in film.select('.score i')])

        yield item


def write_to_json(item):
    with open('result.txt', 'a') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(page):
    url = 'http://maoyan.com/board/4?offset=' + str(page * 10)
    html = get_one_page(url)

    for item in parse_one_page(html):
        write_to_json(item)


if __name__ == '__main__':
    for i in range(10):
        main(i)
