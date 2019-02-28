import json
from lxml import etree
import requests


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    html = etree.HTML(html)
    films = html.xpath('//dl[@class="board-wrapper"]/dd')
    for film in films:
        item = {}
        item['index'] = film.xpath('i/text()')[0]
        item['image'] = film.xpath('a/img[2]/@data-src')[0]
        item['title'] = film.xpath('.//p[@class="name"]/a/text()')[0]
        item['author'] = film.xpath('.//p[@class="star"]/text()')[0].strip()[3:].split(',')
        item['time'] = film.xpath('.//p[@class="releasetime"]/text()')[0][5:]
        item['score'] = ''.join(film.xpath('.//p[@class="score"]/i/text()'))
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
