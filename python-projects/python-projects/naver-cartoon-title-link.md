# Naver Cartoon Title & Link

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