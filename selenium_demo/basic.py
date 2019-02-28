import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
search_input = browser.find_element_by_id('q')
search_input.send_keys('iPhone')
time.sleep(2)
search_input.clear()
search_input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
time.sleep(2)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
