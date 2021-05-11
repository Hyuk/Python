# Requests

### How to check the connection with URL
```python
import requests
res = requests.get("http://naver.com")
print("response code: ", res.status_code)

if res.status_code == requests.codes.ok:
  print("connection is ok")
else:
  print("there was a commenction problem")

res.raise_for_status() # if status_code is not 200 then display error and exit
print("starting web scraping")
```

### Display the length of the scrapped text
```python
print(len(res.text))

# 123456
```

### Create a file and Save scrapped text
```python
with open("mywebsite.html","w",encoding="utf8") as f:
  f.write(res.text)
```

### User Agent
* for some website blocking request without headers, we need browser user agent that contains browser header information.
* [Get User Agent Information](https://www.whatismybrowser.com/detect/what-is-my-user-agent)

```python
import requests
url = "http://smilehugo.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.105.22 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("smilehugo.html", "w", encoding="utf8") as f:
  f.write(res.text)
```
