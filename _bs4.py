import  requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res= requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.a)  # soupt 객체에서 처음 발견되는 a태그의 속성
# print(soup.a.attrs) # a element 의 속성 정보
# print(soup.a['href']) # a element의 href속성 정보값값

#print(soup.find("a", attrs={"class" : "Nbtn_upload"}))   # class가 Nbtn-upload인 element를 찾아줘

#print(soup.find("li",attrs={"class" : "rank01"} ))
rank1 = soup.find("li",attrs={"class" : "rank01"} )
# print(rank1.a)
# print(rank1.a.get_text())

rank2 = rank1.find_next_sibling("li") # 개행 있는건 상관없이 rank1의 li태그 다음 것을 가져온다
#print(rank2.a.get_text())

# 하나하나 next_sibling을 하면 힘들다
#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="화이트 블러드-88화")
print(webtoon)