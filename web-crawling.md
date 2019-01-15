# Web Crawling

```
!pip install requests
!pip install bs4
```

```python
import requests

response = requests.get("https://www.naver.com/")
response.text
# 줄바꿈이 안된 형태의 모든 html코드를 보여준다.
"날보러와요" in response.text
# True
from bs4 import BeautifulSoup
bs = BeautifulSoup(response.text, "html.parser")
# response.text를 보다 정렬해서 보여준다.
```