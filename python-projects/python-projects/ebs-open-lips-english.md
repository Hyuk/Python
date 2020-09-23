# EBS Open Lips English

```python
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# //*[@id="ListWap"]/table/tbody/tr[1]/td[3]/a
url = "https://5dang.ebs.co.kr/auschool/detail?courseId=BK0KAKC0000000014&stepId=01BK0KAKC0000000014&lectId=20362041&situ=&pageNum=1&orderByString="
browser.get(url)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(interval)
soup = BeautifulSoup(browser.page_source, "lxml")



mp3file = soup.find("video").get("src")
print(mp3file)
mp3file_res = requests.get(mp3file)
mp3file_res.raise_for_status()

with open("open_lips.mp3","wb") as f:
    f.write(mp3file_res.content)

browser.quit()
```