import time
import requests
from bs4 import BeautifulSoup
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")
#네이버 항공권
browser.get("https://m-flight.naver.com/")

# 가는날 셀레니움으로 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()

# 국내 일본 유럽... 어디든 클라이언트가 원하는 값을 선택하도록 만들기 bs4로 크롤링하기
res = browser.page_source

soup = BeautifulSoup(res, "lxml")

# 버튼 값들 다 가져왔다 list, select랑 find_all이랑 둘다 list로 반환한다
start = soup.select('section > section > button')
want = input('')

# s.text하면 나라들 나온다
# 사용자가 원하는 나라를 클릭
pos = 0
for i, v  in  enumerate(start):
    if v.text == want:
        #browser.find_element('v').send_keys(Keys.ENTER)

        print(i, v)
        print(start[i])
        print(v.text)
        # k = browser.find_element('v')
        # time.sleep(3)
        browser.find_element_by_css_selector('button.autocomplete_Collapse__tP3pM').click()
        #
       #  국내의 copy element랑 print(v) == print(start[i])근데 왜 안되지 ?..
       #<button aria-expanded="false" class="autocomplete_Collapse__tP3pM" type="button">국내</button>
       # browser.find_element_by_css_selector()
       #browser.find_element('<button aria-expanded="false" class="autocomplete_Collapse__tP3pM" type="button">국내</button>').click()

# 도착 하는 나라 누르기
desti = soup.select('section > section > button')
want = input('')
for i, v  in  enumerate(start):
    if v.text == want:
        #browser.find_element('v').send_keys(Keys.ENTER)
        # k = browser.find_element('v')
        # time.sleep(3)
        browser.find_element_by_css_selector('button.autocomplete_Collapse__tP3pM').click()
        browser.find_element_by_css_selector('div.autocomplete_list__de1dI').click()


# 가는 날 클릭
day = soup.select('#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div:nth-child(2)')
go_day = day[0]
# end_day = day[1]
browser.find_element_by_css_selector(go_day).click()
