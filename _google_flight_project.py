import time
import requests
from bs4 import BeautifulSoup
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbThree


def get_info():
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
    end_val = '//*[@id="ow59"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input'
    browser.find_element_by_xpath(end_val).click()
    time.sleep(1)
    browser.find_element_by_xpath(end_val).send_keys(Keys.CONTROL + "a")
    time.sleep(1)
    browser.find_element_by_xpath(end_val).send_keys(Keys.DELETE)
    time.sleep(1)
    browser.find_element_by_xpath(end_val).send_keys(end_day)
    time.sleep(1)
    browser.find_element_by_xpath(end_val).send_keys(Keys.ENTER)
    # 날짜선택 확인 누르기
    time.sleep(2)
    browser.find_element_by_xpath(end_val).click()

    # 비용가지고 오기
    time.sleep(2)
    # elements로 가져와도 길이는 1지만 정보는 다 들어가있다
    elem = browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/div/div/c-wiz/div[2]/div/div[1]/main/div/div[2]/ol')
    elems = elem.find_elements_by_tag_name('li')

    # cnt = 1;
    # for i in elems:
    #     if i.text == "":
    #         break
    #     print(cnt)
    #     cnt += 1
    #     print(i.text)

    time.sleep(10)
    browser.close()

    return elems

# 결정된 날짜와 결정된 도착지 정보 + 금액을 mydb 콜렉션에 저장합니다
def insert_db(info):

    print("insert부분")
    print(info)

    # doc = {
    #     'desti' : desti,
    #     'fee' : fee,
    #     'time' : time
    # }

    # db.mydb.insert_one(doc)
    print('저장 완료')

def insert_all():
    db.mydb.drop()
    info = get_info()
    for i in info:
        if i.text == "":
            break
        insert_db(i.text)

insert_all()

"""
elements 는 해당하는결과의 모든것을 list로 반환
element는 해당값의 첫번째 결과만 element값으로 반환합니다
# elements로 가져와도 길이는 1지만 정보는 다 들어가있다
 elem = driver.find_element_ 솰라솰라
elems = elem.find_elements_by_tag_name('li')

"""