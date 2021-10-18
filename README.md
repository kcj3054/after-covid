#### 수정중입니다. 

#  프로젝트명 : 코로나 이후 여행

코로나 이후 여행 수요가 급증할 것으로 예상됩니다.
본인이 가고싶었던 여행지의 항공권 or 관련 자료들을 저장해보는 프로젝트입니다.


# 프로젝트 구조  

*  세계지도를 띄우고 주요 도시들을 마크합니다.
*  본인이 원하는 곳을 클릭한 후 항공권 정보를 셀레니움을 이용해서 가지고 옵니다.
*  가지고 온 데이터들을 dbThree 내의 mydb 컬렉션에 저장해 놓습니다. 
*  자신만의 여행정보를 저장합니다. 
*  개개인의 정보를 저장하기 위해서 로그인 기능을 구현합니다.

# 목차 
1. 사용기술
2. 핵심 기능
3. 트러블 슈팅

# 사용 기술 및 환경
flsk, javascript, ajax, sellenium, mongodb, jwt, git, aws

# 맴버 구성 
- 김영산, 김창주, 우정윤

# git 브랜치 전략 
git flow를 사용하면서 진행합니다.

- Mastger : 배포시 
- Develop : 개발 중 
- Feature : 기능 개발
- ....

# 개발 기간
2주

# 화면설계
![image](https://user-images.githubusercontent.com/51309615/134605644-6844eeac-f87f-410c-a44e-15f6575daa5d.png)

# 트러블 슈팅
#### 셀레니움 문제 
<details>
<summary>셀레니움시 copy xpath로 값을 찾지 못하거나 화면 화면 변경시 발생하는 에러</summary>
<div markdown="1">
- 셀레니움으로 값을 가져오기를 원하는 부분을 xpath의 link_text를 사용하기도 했습니다. 그러나 모든 부분이 xpath로 먹히지는 않습니다. 그럴 때는 더 상위의 태그를 체킹해보는 시도를 해보아야 합니다.<p>
- 화면 변경시 알 수 없는 에러가 발생하기도 하는데 그 이유는 화면은 전환 했는데 셀레니움은 이전의 화면에서 아직 오지 못했기 때문입니다. 그래서 그 부분을 기다려주기 위해서 tiem.sleep()으로 시간을 주면서 기다려주는 방법이 있습니다.
</div>
</details>
<details>
<summary> .clear()를 실행해도 값이 지워지지 않는 경우</summary>
<div markdown="1">
- 값이 디폴트로 지정되어있는 경우 값을 clear()로 지워서 원하는 값을 입력하는걸로 알고 있었습니다. 그러나 clear가 되지 않는 경우도 있습니다.<p>
- 이럴때는 전체선택과 delete로 clear를 대체해야 합니다.
</div>
</details>

#### 좌표 클릭 문제
<details>
<summary>area태그의 좌표coords의 값이 클릭후 팝업이 뜨지 않았던 이유</summary>
<div markdown="1">
- 처음에 좌표가 클릭이 안 되었던 이유는 이미지 파일의 픽셀이 작았기 때문입니다.<p>
- 초기에 설정한 좌표값이 임의로 지정한 값이라 적용되지 않았습니다.<p>
- https://rgy0409.tistory.com/2881 를 참고하여 좌표값을 지정하는 방법을 알고 지정을 했는데 팝업이 뜨지 않았습니다.<p>
- 팝업이 뜨지 않았던 이유는 세계지도 이미지위에 div태그를 사용하여 런던, 파리, 도쿄 등등의 도시를 대표하는 이미지를 추가로 넣어주어서 클릭이 되지 않았습니다.<p>
- 포토샵으로 해당 도시위치에 대표이미지를 합성해서 새로운 worldmap.png를 만들어 div 태그들을 없애주었습니다.
</div>
</details>

#### https로 접속시 마이크 차단 현상 
<details>
<summary>https로 접속시 마이크 차단 현상</summary>
<div markdown="1">
- 각각의 파일로 돌렸을때는 구글에서 마이크 차단현상이 없었습니다.<p>
- 하지만 같이 돌리면서 flask로 돌릴경우 마이크 차단현상이 있었습니다. -> cors 정책문제인걸 인지 후 해결. 
</div>
</details>

#### local에서 접속시 html파일들이 4xx 에러가 발생
<details>
<summary>localhost에서 페이지가 안 띄워지는 오류</summary>
<div markdown="1">
- 해당 파일을 개별적으로 실행했을때는 실행이 되지만 서버로 돌릴 경우 에러가 발생했습니다.<p>
- 해당 이유는 에러가 발생하는 html 파일들을 렌더링을 제대로 하지 못했기 때문입니다.
</div>
</details>

#### 항공권 셀레니움 작동 테스트시 에러
<details>
<summary>항공권 셀레니움이 되는 국가 및 도시가 한정적임</summary>
<div markdown="1">
- 해당 이유는 저는 항공권이 있는 화면 url을 가리키고 있었는데 오류가 나는 화면에서는 코로나로인해 입국이 금지된 화면이라서 항공정보가 없어서 에러가 발생했습니다.<p>
- 입국금지가 된 여행지를 제외하고는 정상 작동이 됩니다.
</div>
</details>

#### 로그인 기능 구현 시 에러
<details>
<summary>jwt 라이브러리 에러</summary>
<div markdown="1">
- 기존에 설치되어 있었던 pyjwt 라이브러리와 충돌이 일어남.<p>
- jwt 라이브러리를 삭제.
</div>
</details>

#### places 목록 불러올 때 에러
<details>
<summary>장소 검색 후 목록을 불러올 때 기존 목록에 더해지는 에러</summary>
<div markdown="1">
- 해당 목록의 ul 아이디인 $('#places)를 특정함.<p>
- showMap 함수 내 service.nearbySearch 실행 전 $('#places').empty()를 넣어줌.
</div>
</details>

#### bookmark 크롤링 기능 구현 시 에러
<details>
<summary>크롤링을 위한 URL을 넘겨주는 과정에서 에러</summary>
<div markdown="1">
- placeIdElement의 id 속성을 이용해 $('#PlaceId').href로 URL을 정의함.<p>
- addPlaces 함수 밖에서 호출하니 id 만으로는 URL이 불러와지지 않음.<p>
- save_venues 함수를 addPlaces 안에서 호출 및 PlaceIdElement.href로 URL을 재정의.
</div>
</details>

#### 네비바 css 에러
<details>
<summary>test.html 파일에서 네비바에 css가 안 먹히는 에러</summary>
<div markdown="1">
- css 파일을 보니 이미 모든 ul에 대해서 적용된 css가 존재.<p>
- div를 따로 줘서 해결하려고 했으나 여전히 css가 적용되지 않음.<p>
- li 태그의 내용물인 a 태그만 남기고 ul 및 li 태그는 삭제.
</div>
</details>

#### URL에 a 태그 적용하기
<details>
<summary>addPlaces 함수 내 infowindow에서 URL에 a 태그가 안 먹힘</summary>
<div markdown="1">
- a 태그를 적용하기 위해 creatTextNode, appendChild 속성을 이용함
</div>
</details>

#### 구글맵스 api 페이지 분리
<details>
<summary>메인페이지의 search box 검색 시 지도페이지로 이동하는 기능 구현 시 에러</summary>
<div markdown="1">
- 메인페이지에서 initautocomplete으로 위도와 경도 값을 받아서 지도페이지에 넘겨줌.<p>
- 받아온 위도, 경도 값에 +를 붙여서 좌표 에러가 뜨는 것을 해결함.
</div>
</details>
