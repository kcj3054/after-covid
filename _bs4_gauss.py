import  requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list?titleId=675554"
res= requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#cartoons = soup.find_all("td", attrs={"class" : "title"})
#print(cartoons)
#title = cartoons[1].a.get_text()
#link = cartoons[1].a["href"]
#print(title)
#print("https://comic.naver.com/" +link)

# 만화정보와 링크가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link =  cartoon.a["href"]
#     print(title, "https://comic.naver.com/" + link)

# 평점가져오기
total_tates = 0
cartoons  = soup.find_all("div", attrs={"class" : "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
