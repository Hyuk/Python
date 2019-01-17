# Web Crawling

```
!pip install requests
!pip install bs4
```

```python
import requests

response = requests.get("https://www.naver.com/")
response.text
# 줄바꿈이 안된 형태의 모든 html코드를 보여준다.

"날보러와요" in response.text
# True

from bs4 import BeautifulSoup
bs = BeautifulSoup(response.text, "html.parser")
# response.text를 보다 정렬해서 보여준다.
```


## 네이버 실시간 검색어 순위 크롤링 하기
```python
response = request.get("https://www.naver.com/")
bs = BeautifulSoup(response.text, "html.parser")
elements = bs.select("ul.ah_l li.ah_item span.ah_k")
element = elements[0]
element.text

# 실시간 검색어 순위 1위를 가져온다
```

```python
response = requests.get("https://www.naver.com/") 
bs = BeautifulSoup(response.text, "html.parser")
elements = bs.select("div.ah_roll_area ul.ah_l li.ah_item span.ah_k")
[
    element.text
    for element in elements
]

# 실시간 검색어 순위를 리스트 형태로 반환한다.
# list comprehension.
'''
['정재일',
 '너의 노래는',
 '김학래',
 '가수 김학래',
 '이원근',
 '신성우',
 '신지예',
 '시간이탈자',
 '기무라타쿠야',
 '일본 우즈베키스탄',
 '라라츄 헤어쿠션',
 '기태영',
 '구준엽 오지혜',
 '유호정',
 '위메프 슈퍼특가데이',
 '이준석',
 '오지혜',
 '이성미',
 '박효신',
 '하연수']
 '''
```

## 파이썬 블로그 검색 결과 리스트
```python
response = requests.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
bs = BeautifulSoup(response.text,"html.parser")
elements = bs.select("a.sh_blog_title")
element = elements[0]

[
    element.text
    for element in elements
]

# ['삼성이 챙기는 파이썬',
#  '"진정한 파이썬 고급 개발자가 되기 위한 능력을...',
#  '파이썬 IDE - 파이참(PyCharm) 설치 하기.',
#  '파이썬학원 추천 프로그래밍 기초수업강의!',
#  'I7 8700.GTX1060 배그 조립컴퓨터.파이썬. C언어 공부.청주...',
#  '[도서리뷰] Django로 배우는 쉽고 빠른 웹개발[파이썬 웹...',
#  '파이썬(python) 공부하기 20 – 기타등등에 관한 이야기',
#  '[파이썬] 윈도우10에서 jupyter lab 이용하기',
#  '[파이썬 초급] 이진검색 ④ 유사코드 만들기',
#  'Python(파이썬) 설치 방법']


```

```python
# request 가 막힐때
response = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=2019+%EC%95%84%EC%8B%9C%EC%95%88%EC%BB%B5+%ED%95%9C%EA%B5%AD%EC%B6%95%EA%B5%AC+%EC%9D%BC%EC%A0%95",headers={
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36 Safari/601.1"
})
```


```python
# 브라우저 자동화 방법
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("https://~")
from IPython.display import Image
Image(driver.get_screenshot_as_png())

```

## 데이터 베이스 연결해서 데이터 추출
```python
import MySQLdb
db = MySQLdb.connect(
    "db.fastcamp.us", # DATABSE_HOST
    "root", # DATABASE_USERNAME
    "dkstncks", # DATABASE_PASSWORD
    "sakila", # DATABASE_NAME
    charset='utf8',
)

SQL_QUERY = """
    SELECT *
    FROM customer
    ;
"""

pd.read_sql(SQL_QUERY, db)

```