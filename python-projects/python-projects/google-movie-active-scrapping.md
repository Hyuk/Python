# Google Movie Active Scrapping

```python
import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/top'
headers = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36",
  "Accept-Language":"ko-KR,ko"
}

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html","w", encoding="utf8") as f:
#   #f.write(res.text)
#   f.write(soup.prettify())

for movie in movies:
  title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
  print(title)

```

Selenium으로 변환

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://play.google.com/store/movies/top')

# Scroll Down
# browser.execute_script("window.scrollTo(0,1080)") # 1920 x 1080
# browser.execute_script("window.scrollTO(0, document.body.scrollHeight)")

import time
interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  time.sleep(interval)
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if curr_height == prev_height:
    break
  prev_height = curr_height
print("Complete Scroll")
browser.get_screenshot_as_file("google_movie.png") # Take a Screenshot
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
  title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
  # print(title)
  original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
  if original_price:
    original_price = original_price.get_text()
  else:
    # print(title,'except no discount movie')
    continue
  
  price = movie.find("span", attrs={"class","VfPpfd ZdBevf i5DZme"}).get_text()

  link = movie.find("a", attrs={"class","JC71ub"})["href"]

  print(f"Title: {title}")
  print(f"Before Price: {original_price}")
  print(f"After Price: {price}")
  print("Link: ", "https://play.google.com" + link)
  print("-"*100)

browser.quit()
#
"""
Complete Scroll
200
Title: 강철비2 정상회담
Before Price: ₩10,000
After Price: ₩7,000
Link:  https://play.google.com/store/movies/details/%EA%B0%95%EC%B2%A0%EB%B9%842_%EC%A0%95%EC%83%81%ED%9A%8C%EB%8B%B4?id=EiNJ9TtZ68Q.P
----------------------------------------------------------------------------------------------------
Title: 뮬란_중국판
Before Price: ₩10,000
After Price: ₩5,000
Link:  https://play.google.com/store/movies/details/%EB%AE%AC%EB%9E%80_%EC%A4%91%EA%B5%AD%ED%8C%90?id=YUQTvr17iZw.P
----------------------------------------------------------------------------------------------------
Title: 온워드: 단 하루의 기적
Before Price: ₩11,000
After Price: ₩4,400
Link:  https://play.google.com/store/movies/details/%EC%98%A8%EC%9B%8C%EB%93%9C_%EB%8B%A8_%ED%95%98%EB%A3%A8%EC%9D%98_%EA%B8%B0%EC%A0%81?id=fCwq2DL1fDY.P
----------------------------------------------------------------------------------------------------
Title: 존윅 3: 파라벨룸
Before Price: ₩6,500
After Price: ₩5,000
Link:  https://play.google.com/store/movies/details/%EC%A1%B4%EC%9C%85_3_%ED%8C%8C%EB%9D%BC%EB%B2%A8%EB%A3%B8?id=eDVvg9VQfwc.P
----------------------------------------------------------------------------------------------------
Title: 콜 오브 와일드
Before Price: ₩4,500
After Price: ₩2,500
Link:  https://play.google.com/store/movies/details/%EC%BD%9C_%EC%98%A4%EB%B8%8C_%EC%99%80%EC%9D%BC%EB%93%9C?id=SjyZR7ruUGw.P
----------------------------------------------------------------------------------------------------
Title: 인비저블맨
Before Price: ₩1,800
After Price: ₩1,000
Link:  https://play.google.com/store/movies/details/%EC%9D%B8%EB%B9%84%EC%A0%80%EB%B8%94%EB%A7%A8?id=rJ85h-bEzfI.P
----------------------------------------------------------------------------------------------------
Title: 진격의 거인 크로니클
Before Price: ₩10,000
After Price: ₩4,500
Link:  https://play.google.com/store/movies/details/%EC%A7%84%EA%B2%A9%EC%9D%98_%EA%B1%B0%EC%9D%B8_%ED%81%AC%EB%A1%9C%EB%8B%88%ED%81%B4?id=b4D49CmeJnE.P
"""
```
