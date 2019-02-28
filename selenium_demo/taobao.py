from urllib.parse import quote
import pymysql
from lxml import etree
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 10)

host = 'localhost'
port = 3306
user = 'root'
password = '12345678'

db = pymysql.connect(host=host, port=port, user=user, password=password)


def index_page(page, keyword):
    """
    抓取索引页
    :param keyword
    :param page
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q={}'.format(quote(keyword))
        browser.get(url)
        if page > 1:
            page_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.J_Input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.J_Submit')))
            page_input.clear()
            page_input.send_keys(page)
            submit.click()

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page, keyword)


def get_products():
    html = browser.page_source
    tree = etree.HTML(html)
    items = tree.xpath('//div[@data-category="auctions"]')
    for item in items:
        product = {
            'image': 'http:' + item.xpath('normalize-space(.//img[contains(@class, "J_ItemPic")]/@data-src)'),
            'price': item.xpath('normalize-space(string(.//div[@class="price g_price g_price-highlight"]))'),
            'deal': item.xpath('normalize-space(.//*[@class="deal-cnt"]/text())'),
            'title': item.xpath('normalize-space(string(.//*[@class="J_ClickStat"]))'),
            'shop': item.xpath('normalize-space(.//*[contains(@class, "shopname")]/span[last()]/text())'),
            'location': item.xpath('normalize-space(.//*[@class="location"]/text())')
        }
        save_to_mysql(product)


def save_to_mysql(item):
    table = 'taobao'
    keys = ','.join(item.keys())
    values = ','.join(['%s'] * len(item))
    cursor = db.cursor()
    sql = 'insert into spider.{table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
    try:
        cursor.execute(sql, tuple(item.values()))
        db.commit()
    except Exception:
        db.rollback()


if __name__ == '__main__':
    MAX_PAGE = 100
    keyword = 'iPad'
    for i in range(1, MAX_PAGE + 1):
        index_page(i, keyword)
