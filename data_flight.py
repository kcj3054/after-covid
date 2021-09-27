from urllib.parse import quote_plus, urlencode
from urllib import parse
from urllib.request import Request, urlopen

import requests
from bs4 import BeautifulSoup

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
