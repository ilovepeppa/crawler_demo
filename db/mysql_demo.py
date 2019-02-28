import pymysql
from lxml import etree
import requests

host = 'localhost'
port = 3306
user = 'root'
password = '12345678'

db = pymysql.connect(host=host, port=port, user=user, password=password)


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


def save_to_mysql(item):
    cursor = db.cursor()
    sql = ("insert into spider.maoyan(`rank`, `image`, `title`, `author`, `time`, `score`) " +
           "values (%s, %s, %s, %s, %s, %s)")
    try:
        cursor.execute(sql, (item['index'], item['image'], item['title'],
                             ','.join(item['author']),
                             item['time'], item['score']))
        db.commit()
    except Exception:
        db.rollback()


def main(page):
    url = 'http://maoyan.com/board/4?offset=' + str(page * 10)
    html = get_one_page(url)
    for item in parse_one_page(html):
        save_to_mysql(item)


if __name__ == '__main__':
    for i in range(10):
        main(i)
