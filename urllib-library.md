# Library - urllib

* 파일을 입력받아 표시한다
```python
import urllib.request
file = urllib.request.urlopen('https://github.com/Hyuk/Python/blob/master/sample.txt')
message = file.read()
print message
```