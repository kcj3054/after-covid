import time

import requests
from bs4 import BeautifulSoup
from  selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://m-flight.naver.com/"

res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
browser.get("https://beta-flight.naver.com/")

# find_element_by_link_text() 링크텍스트랑 일치하는 첫번째를 가지고온다, a태그만 가능하다
# 가는 날 선택
#browser.find_element_by_link_text("가는 날").click()
time.sleep(1)
#browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(1)
# 다음달 27일, 28일 선택
#browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button').click()

time.sleep(1)
#browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/button').click()

# 도착 선택
time.sleep(1)
#browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()

# 중국으로 가자
time.sleep(1)
countrys = soup.find_all("button", attrs= {"class" : "autocomplete_Collapse__tP3pM"})
print(coun)