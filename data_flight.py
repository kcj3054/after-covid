from urllib.parse import quote_plus, urlencode
from urllib import parse
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup
import re
url = 'http://openapi.airport.co.kr/service/rest/AirportCodeList/getAirportCodeList'
queryParams = '?' + 'ServiceKey=' +'tczAARILXCELP0k8%2F%2FVvXLud8T8G2f%2FxL4eYeBd4EH2cREYEKcOJo0VcLL5eSJVAphD7%2BEOgW3FVLEHBebBp8w%3D%3D'

url = url + queryParams
result = requests.get(url)
soup = BeautifulSoup(result.text, 'lxml')
# soup.select('상위태그명 > 하위태그명 > 하위태그명')
items = soup.select('items > item > cityKor')
# items = soup.find_all("item", attrs={"class" : "클래스명"}) # item이라는 태그 안에 cityKor태그 값을 가지고 와야한다
# soup = BeautifulSoup(res.text, "lxml")
for item in items:
    print(item.text)


# ca?e
# care, cafe, case, cave.. 사고가 나서 기억이 안난다

p = re.compile("ca.e")
p = re.compile("$원")

#. : 하나의 문자를 의미 , ^ : 문자열의 시작
# $(se$) : 문자열의 끝 > case, base(0)
# p.match("case")

def print_match(m):
    m = p.match("caffe")

    if m:
        print(m.group())  # 일치하는 문자열 반환
        print(m.string) #입력받은 문자열
        print(m.start()) # 일치하는 문자열의 시작 index
        print(m.end()) # 일치하는 문자열의 끝 인덱스

    else:
        print("매칭되지 않음")

m = p.search("good care")   # search :  주어진 문자열 중에 일치하는게 있는지 확인
m = p.findall("careless") #findall : 일치하는 모든 것을 리스트형태로 반환