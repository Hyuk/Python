# Selenium

* Download Chrome Driver.
* Chrome Driver Version should be the same as your chrome browser.

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

# Naver Login
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