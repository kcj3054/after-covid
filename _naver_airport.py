import  requests
from bs4 import BeautifulSoup

url = "https://m-flight.naver.com/"

res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

day = soup.find_all("td", attrs={"class" : "day"})
print(day)