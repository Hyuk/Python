# Daum Real Estate

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://daum.net')

elem = browser.find_element_by_name("q")
elem.send_keys("송파 헬리오시티")
elem.send_keys(Keys.ENTER)
```

### 2
```python
import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

with open("quiz.html","w", encoding="utf8") as f:
  f.write(soup.prettify())
```