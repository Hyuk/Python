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