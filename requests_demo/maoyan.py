import re
import json
import requests


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile(
        r'<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?)".*?alt="(.*?)".*?star">\s+(.*?)\s+<.*?releasetime">(.*?)<.*?integer">(\d\.).*?(\d).*?>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'author': item[3][3:].split(','),
            'time': item[4][5:],
            'score': item[5] + item[6]
        }


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
