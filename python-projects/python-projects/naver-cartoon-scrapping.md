# Naver Cartoon Scrapping

### List of Cartoon

```python
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
  print(cartoon.get_text())
```

### Cartoon Series Title & Link

```python
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=733274"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
for cartoon in cartoons:
  title = cartoon.a.get_text()
  link = "https://comic.naver.com" + cartoon.a["href"]
  print(title, link)
```

### Naver Cartoon Review Average

```python
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=733274"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
  rate = cartoon.find("strong").get_text()
  print(rate)
  total_rates += float(rate)

print("Total: ", total_rates)
print("Average: ", total_rates / len(cartoons))
```