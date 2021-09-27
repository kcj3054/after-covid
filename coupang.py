from bs4 import BeautifulSoup
import re
import requests

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent"
res  = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print("a")

# 태그가 li이면서, class가 search-product로 시작하는 것
items = soup.find_all("li", attrs={"class" : "search-product-wrap-img"})
print(items)
