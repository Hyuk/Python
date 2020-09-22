# Selenium

* Download Chrome Driver.
* Chrome Driver Version should be the same as your chrome browser.

* [Selenium with Python](https://selenium-python.readthedocs.io/)

### Installation
```bash
$ pip install selenium
```

### Basic Usage
```python
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://www.naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.back()
browser.forward()
browser.refresh()
browser.back()

elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys
elem.send_keys("노트북")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_tag_name("a")

elem = browser.find_elements_by_tag_name("a")

for e in elem:
    e.get_attribute("href")

browser.get("https://www.daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("노트북")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

browser.close()
browser.quit()
```

### Naver Login
```python
import time
from selenium import webdriver

browser = webdriver.Chrome() # webdriver.Chrome(./chromedriver.exe)

# Go to the naver.com
browser.get("https://www.naver.com")

# Click the login button
browser.find_element_by_class_name("link_login").click()

# Fill out ID & Password
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# Click the login button
browser.find_element_by_id("log.login").click()

time.sleep(3)

# Fill out new ID & Password
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# Print html document
print(browser.page_source)

# Take a screenshot
browser.get_screenshot_as_file("google_movie.png")

# Close current browser tab
browser.close()

# Quit current browser
browser.quit()
```

### Headless Chrome

* Headless Chrome의 경우, User Agent의 값을 받아올때 headless-chrome 정보가 표시되므로 접근이 금지될 수 있다.
* 따라서 options.add_argument로 브라우저의 User Agent 값을 지정해서 넘긴다.

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/85.0.4183.102 Safari/537.36
```