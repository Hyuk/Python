# File I/O - File Input / Output

## 모드
* 읽기 모드: r (read)
* 쓰기 모드(기존 파일 삭제): w (write)
* 추가 모드(파일 생성 또는 추가): a (append)
* .. : 상대 경로
* . : 절대 경로
* 기타 : https://docs.python.org/3.7/library/functions.html#open

## 파일 읽기
* open(), read(), close()
* resource/review.txt
```text
The film, projected in the form of animation,
imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
which eventually paves the path for gaining a fresh perspective on an age-old problem.
The story also happens to centre around two parallel characters, Shundi King and Hundi King,
who are twins, but they constantly fight over unresolved issues planted in their minds
by external forces from within their very own units.
```

```python
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
f.close()
# The film, projected in the form of animation,
# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# which eventually paves the path for gaining a fresh perspective on an age-old problem.
# The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# who are twins, but they constantly fight over unresolved issues planted in their minds
# by external forces from within their very own units.
```

* 읽기 모드에 어떤 기능이 있는지 살펴볼때
```python
f = open('./resource/review.txt', 'r')
content = f.read()
print(dir(f))
f.close()
# ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
```

* test.txt
```text 
hellow world
python programming
한글
```

```python
fp = open("test.txt", "r")
data = fp.read()
print(data)
fp.close()
# hellow world
# python programming
# 한글
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




## with
with와 함께 open 문을 실행하면 close가 필요없이 블락이 끝나면 자동으로 닫힌다.
```python 
with open("./animals.csv") as fp:
    data = fp.read()
print(data)
```

```python
with open('./resource/review.txt', 'r') as f:
    c = f.read()
print(c)
# The film, projected in the form of animation,
# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# which eventually paves the path for gaining a fresh perspective on an age-old problem.
# The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# who are twins, but they constantly fight over unresolved issues planted in their minds
# by external forces from within their very own units.

print(list(c))
# ['T', 'h', 'e', ' ', 'f', 'i', 'l', 'm', ',', ' ', 'p', 'r', 'o', 'j', 'e', 'c', 't', 'e', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 'f', 'o', 'r', 'm', ' ', 'o', 'f', ' ', 'a', 'n', 'i', 'm', 'a', 't', 'i', 'o', 'n', ',', '\n', 'i', 'm', 'p', 'a', 'r', 't', 's', ' ', 't', 'h', 'e', ' ', 'l', 'e', 's', 's', 'o', 'n', ' ', 'o', 'f', ' ', 'h', 'o', 'w', ' ', 'w', 'a', 'r', 's', ' ', 'c', 'a', 'n', ' ', 'b', 'e', ' ', 'e', 'l', 'u', 'd', 'e', 'd', ' ', 't', 'h', 'r', 'o', 'u', 'g', 'h', ' ', 'r', 'e', 'a', 's', 'o', 'n', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'p', 'e', 'a', 'c', 'e', 'f', 'u', 'l', ' ', 'd', 'i', 'a', 'l', 'o', 'g', 'u', 'e', 's', ',', '\n', 'w', 'h', 'i', 'c', 'h', ' ', 'e', 'v', 'e', 'n', 't', 'u', 'a', 'l', 'l', 'y', ' ', 'p', 'a', 'v', 'e', 's', ' ', 't', 'h', 'e', ' ', 'p', 'a', 't', 'h', ' ', 'f', 'o', 'r', ' ', 'g', 'a', 'i', 'n', 'i', 'n', 'g', ' ', 'a', ' ', 'f', 'r', 'e', 's', 'h', ' ', 'p', 'e', 'r', 's', 'p', 'e', 'c', 't', 'i', 'v', 'e', ' ', 'o', 'n', ' ', 'a', 'n', ' ', 'a', 'g', 'e', '-', 'o', 'l', 'd', ' ', 'p', 'r', 'o', 'b', 'l', 'e', 'm', '.', '\n', 'T', 'h', 'e', ' ', 's', 't', 'o', 'r', 'y', ' ', 'a', 'l', 's', 'o', ' ', 'h', 'a', 'p', 'p', 'e', 'n', 's', ' ', 't', 'o', ' ', 'c', 'e', 'n', 't', 'r', 'e', ' ', 'a', 'r', 'o', 'u', 'n', 'd', ' ', 't', 'w', 'o', ' ', 'p', 'a', 'r', 'a', 'l', 'l', 'e', 'l', ' ', 'c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r', 's', ',', ' ', 'S', 'h', 'u', 'n', 'd', 'i', ' ', 'K', 'i', 'n', 'g', ' ', 'a', 'n', 'd', ' ', 'H', 'u', 'n', 'd', 'i', ' ', 'K', 'i', 'n', 'g', ',', '\n', 'w', 'h', 'o', ' ', 'a', 'r', 'e', ' ', 't', 'w', 'i', 'n', 's', ',', ' ', 'b', 'u', 't', ' ', 't', 'h', 'e', 'y', ' ', 'c', 'o', 'n', 's', 't', 'a', 'n', 't', 'l', 'y', ' ', 'f', 'i', 'g', 'h', 't', ' ', 'o', 'v', 'e', 'r', ' ', 'u', 'n', 'r', 'e', 's', 'o', 'l', 'v', 'e', 'd', ' ', 'i', 's', 's', 'u', 'e', 's', ' ', 'p', 'l', 'a', 'n', 't', 'e', 'd', ' ', 'i', 'n', ' ', 't', 'h', 'e', 'i', 'r', ' ', 'm', 'i', 'n', 'd', 's', '\n', 'b', 'y', ' ', 'e', 'x', 't', 'e', 'r', 'n', 'a', 'l', ' ', 'f', 'o', 'r', 'c', 'e', 's', ' ', 'f', 'r', 'o', 'm', ' ', 'w', 'i', 't', 'h', 'i', 'n', ' ', 't', 'h', 'e', 'i', 'r', ' ', 'v', 'e', 'r', 'y', ' ', 'o', 'w', 'n', ' ', 'u', 'n', 'i', 't', 's', '.']

print(iter(c))
# <str_iterator object at 0x000002BAE834DE50>
```

```python
with open('./resource/review.txt','r') as f:
    for c in f:
        print(c)
# The film, projected in the form of animation,

# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,

# which eventually paves the path for gaining a fresh perspective on an age-old problem.

# The story also happens to centre around two parallel characters, Shundi King and Hundi King,

# who are twins, but they constantly fight over unresolved issues planted in their minds

# by external forces from within their very own units.
```

* 위에서 문장과 문장 사이에 나타나는 빈줄을 없애려면 다음과 같이 작성한다.
```python
with open('./resource/review.txt','r') as f:
    for c in f:
        print(c.strip())
# The film, projected in the form of animation,
# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# which eventually paves the path for gaining a fresh perspective on an age-old problem.
# The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# who are twins, but they constantly fight over unresolved issues planted in their minds
# by external forces from within their very own units.
```

* read를 두번 이상 사용할 경우, 첫번째 read만 실행된다.
```python
with open('./resource/review.txt','r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음 # 첫번째 실행된 read에서 커서가 파일의 맨 마지막으로 이동했기 때문
    print(">", content)
```

* 줄단위로 읽기
```python
with open('./resource/review.txt','r') as f:
    line = f.readline() # 한 줄을 읽는다.
print(line)
# The film, projected in the form of animation,
```

* 줄단위로 읽는 기능에 반복문을 적용
```python
with open('./resource/review.txt','r') as f:
    line = f.readline()
    while line:
        print(line, end=' ##### ')
        line = f.readline()
# The film, projected in the form of animation,
# ##### imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# ##### which eventually paves the path for gaining a fresh perspective on an age-old problem.
# ##### The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# ##### who are twins, but they constantly fight over unresolved issues planted in their minds
# ##### by external forces from within their very own units. ##### 
```

* readlines 
* 줄 단위를 리스트 형태로 반환한다.
```python
with open('./resource/review.txt','r') as f:
    line = f.readlines()
print(line)
```

* readlines - for statement
```python
with open('./resource/review.txt','r') as f:
    line = f.readlines()
    for c in line:
        print(c)

# The film, projected in the form of animation,

# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,

# which eventually paves the path for gaining a fresh perspective on an age-old problem.

# The story also happens to centre around two parallel characters, Shundi King and Hundi King,

# who are twins, but they constantly fight over unresolved issues planted in their minds

# by external forces from within their very own units.
```

* 빈칸을 지우려면
```python
with open('./resource/review.txt','r') as f:
    line = f.readlines()
    for c in line:
        print(c.strip())
# The film, projected in the form of animation,
# imparts the lesson of how wars can be eluded through reasoning and peaceful dialogues,
# which eventually paves the path for gaining a fresh perspective on an age-old problem.
# The story also happens to centre around two parallel characters, Shundi King and Hundi King,
# who are twins, but they constantly fight over unresolved issues planted in their minds
# by external forces from within their very own units.
```

* 텍스트 파일의 숫자의 평균
```python
with open('./resource/score.txt','r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print('Average : {:6.3}'.format(sum(score)/len(score)))
# Average :   86.7
```



## 파일 쓰기
```python
fp = open("second.txt","w")
fp.write("Hello World\n두번째 파일")
fp.close()
```

* error
* 한글로 파일을 쓸때 다음과 같은 오류 메세지를 보게 될 경우
```text
Error! second.txt is not UTF-8 encoded
Savign disabled.
See Console for more details.
```
* encoding 값 UTF-8으로 지정해준다.
```python
fp = open("second.txt","w",encoding="UTF-8")
fp.write("Hello World\n두번째 파일")
fp.close()
```

* 파일 쓰기 모드 with 로 사용하기
* 파일이 없을 경우, 글자를 넣어 새로 파일을 만든다.
```python
with open('./resource/text1.txt','w') as f:
    f.write('Niceman!')
```

## 파일 추가 모드
* 파일 끝에 글자를 추가한다.
```python
with open('./resource/text1.txt','a') as f:
    f.write('Goodman!')
```

```python
from random import randint

with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 34
# 19
# 28
# 44
# 42
# 36
```

### writelines: 리스트 -> 파일로 저장
```python
with open('./resource/text3.txt','w') as f:
    list = ['Kim\n','Park\n','Cho\n']
    f.writelines(list)
```

* text3.txt
```
# Kim
# Park
# Cho
# 
```

### print함수 사용해서 파일로 저장하기
```python
with open('./resource/text4.txt','w') as f:
    print('Test Contest1!', file=f)
    print('Test Contest2!', file=f)
```
* text4.txt
```text
Test Contest1!
Test Contest2!
```