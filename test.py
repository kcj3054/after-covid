import time
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@13.125.216.47', 27017)
client = MongoClient('localhost', 27017)
db = client.dbThree
#
def insert_all():
    db.mydb.drop()
    browser = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
    browser.maximize_window()
    url = 'https://www.google.com/flights'
    browser.get(url)
    # 출발
    go_want = input('')
    browser.find_element_by_xpath('//*[@id="i6"]/div[1]/div/div/div[1]/div/div/input').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.CONTROL + "a")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.DELETE)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(go_want)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)

    # 도착
    go_desti = input('')
    browser.find_element_by_xpath('//*[@id="i6"]/div[4]/div/div/div[1]/div/div/input').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(go_desti)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="i6"]/div[6]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)

    # 날짜선택하기
    start_day = input('')
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input').click()
    time.sleep(1)
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input').clear()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').send_keys(
        Keys.CONTROL + "a")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').send_keys(
        Keys.DELETE)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').send_keys(
        start_day)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input').send_keys(
        Keys.ENTER)

    end_day = input('')
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(
        Keys.CONTROL + "a")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(
        Keys.DELETE)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(end_day)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input').send_keys(
        Keys.ENTER)
    # 날짜선택 확인 누르기
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="ow59"]/div[2]/div/div[3]/div[3]/div/button/span').click()

    # 검색 누르기
    # time.sleep(1)
    # browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[2]/div/button/span[2]').click()

    # 비용가지고 오기
    # time.sleep(1)
    time.sleep(3)
    # //*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/div/div/c-wiz/div[2]/div/div[1]/main/div/div[2]/ol
    elem = browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/div/div/c-wiz/div[2]/div/div[1]/main/div/div[2]/ol')
    elems = elem.find_elements_by_tag_name('li')
    # 나라, 금액,
    # 출발날짜 db에 다 담아야한다

    p = re.compile("^\ ")
    cnt = 1;
    print(go_want, go_desti)
    print(start_day, end_day)
    info = list()
    # 디버깅 테스트용 반복문
    for i in elems:
        if i.text == "" or len(i.text) < 10:
            break
        print(cnt)
        cnt += 1
        info.append(i.text)

    time.sleep(10)
    browser.close()

    doc = {
        'desti': go_desti,
        'go_want': go_want,
        'start_day': start_day,
        'end_day': end_day,
        'info': info
    }

    db.mydb.insert_one(doc)
insert_all()
