# Beautifulsoup4
* library for web scraping

### installation
```bash
$ pip install beautifulsoup4
```


```python
import requesets
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title)

# <title>네이버 만화 &gt; 요일별 웹툰 &gt; 전체웹툰</title>

print(soup.title.get_text())

# 네이버 만화 &gt; 요일별 웹툰 &gt; 전체웹툰

print(soup.a)

# print first a tag in the scrapped text

print(soup.a.attrs)

# {'href':'#menu',"onclick':'document.getElementById('menu')"}

print(soup.a["href"])

# #menu

print(soup.find("a", attrs={"class":"Nbtn_upload"}));

# <a class="Nbtn_upload"></a>

print(soup.find(attrs={"class":"Nbtn_upload"}))

print(soup.fint(attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text())
print(rank1.next_sibling.next_sibling)

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
print(rank1.parent)
rank2 = rank1.find_next_sibling("li")
print(rank2.a.get.text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get.text())

print(rank1.find_next_siblings("li").a.get.text())

webtoon = soup.find("a", text="some text")
print(webtoon)

# <a>some text</a>
```

### find
* find the first tag that scrapped text

### find_all
* find the all tags that scrapped text


```python
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
request = requests.get(url)
res.raise_For_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("a", attrs={"class":"title"})

for cartoon in cartoons:
  print(cartoon.get_text())
```