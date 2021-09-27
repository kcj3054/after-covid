import time
import requests
from bs4 import BeautifulSoup
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
browser.maximize_window()
url = 'https://www.google.com/flights'
browser.get(url)

go_want = input('')
# 출발
browser.find_element_by_xpath('//*[@id="i6"]/div[1]/div/div/div[1]/div/div/input').click()
browser.find_element_by_xpath('//*[@id="i6"]/div[1]/div/div/div[1]/div/div/input').clear()
browser.find_element_by_xpath('//*[@id="i6"]/div[1]/div/div/div[1]/div/div/input').send_keys(go_want)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)

time.sleep(1)

go_desti = input('')
# 도착
browser.find_element_by_xpath('//*[@id="i6"]/div[4]/div/div/div[1]/div/div/input').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(go_desti)
browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)

#날짜선택하기
time.sleep(1)
# browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div').click()
# browser.find_element_by_link_text('19').click()
# browser.find_element_by_link_text('20').click()

#검색 누르기
time.sleep(1)
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[2]/div/button/span[2]').click()


# 비용가지고 오기
time.sleep(1)
elem = browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/div/div/c-wiz/div[2]/div/div[1]/main/div/div[2]/ol')

time.sleep(1)


print(elem.text)

