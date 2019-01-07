# file management

## 파일 읽기
```
test.txt
hellow world
python programming
한글
```

```python
fp = open("test.txt", "r")
data = fp.read()
data
```

## error
한글로 된 파일을 열때 다음과 같은 오류 메세지를 보게 될 경우
'cp949' codec can't decode byte 0xed in position 32: illegal multibyte sequence

```python
fp = open("test.txt","r",encoding="UTF-8")
data = fp.read()
data
# 'hellow world\npython programming\n한글'
data.split("\n")
# ['hellow world', 'python programming', '한글']
```


## 파일 쓰기
```python
fp = open("second.txt","w")
fp.write("Hello World\n두번째 파일")
fp.close()
```

## error
한글로 파일을 쓸때 다음과 같은 오류 메세지를 보게 될 경우
Error! second.txt is not UTF-8 encoded
Savign disabled.
See Console for more details.

```python
fp = open("second.txt","w",encoding="UTF-8")
fp.write("Hello World\n두번째 파일")
fp.close()
```