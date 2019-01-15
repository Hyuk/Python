# Library

## Pandas
* 파일 입출력시 사용된다

### Jupyter Notebook에서 Pandas Library를 Import하지 못할때
jupyter notebook에서 다음 구문을 실행하면 pandas가 설치된다.
```python
!pip install pandas

# Collecting pandas
#   Downloading https://files.pythonhosted.org/packages/26/fc/d0509d445d2724fbc5f9c9a6fc9ce7da794873469739b6c94afc166ac2a2/pandas-0.23.4-cp37-cp37m-win32.whl (6.8MB)
# Collecting pytz>=2011k (from pandas)
#   Downloading https://files.pythonhosted.org/packages/61/28/1d3920e4d1d50b19bc5d24398a7cd85cc7b9a75a490570d5a30c57622d34/pytz-2018.9-py2.py3-none-any.whl (510kB)
# Collecting numpy>=1.9.0 (from pandas)
#   Downloading https://files.pythonhosted.org/packages/42/5a/eaf3de1cd47a5a6baca41215fba0528ee277259604a50229190abf0a6dd2/numpy-1.15.4-cp37-none-win32.whl (9.9MB)
# Requirement already satisfied: python-dateutil>=2.5.0 in d:\programs\python\python37-32\lib\site-packages (from pandas) (2.7.5)
# Requirement already satisfied: six>=1.5 in d:\programs\python\python37-32\lib\site-packages (from python-dateutil>=2.5.0->pandas) (1.12.0)
# Installing collected packages: pytz, numpy, pandas
# Successfully installed numpy-1.15.4 pandas-0.23.4 pytz-2018.9

```

## OS
```python
import os
from os import listdir

listdir()
# 현재 폴더의 파일을 열거한다
# 또는

import os
os.listdir()
# 현재 폴더의 파일을 열거한다
# 상대경로
os.listdir("./") # 현재폴더
os.listdir("../") # 상위폴더
os.listdir("../../") # 상위폴더의 상위폴더

# 절대경로
os.listdir("D:/hugo")
```
* os.path.join()
```python
os.path.join("../")
# ../
os.listdir(
    os.path.join("../")
)
# 상위폴더의 파일을 리스트 형태로 반환한다.
```

* 폴더에서 txt포맷 형식만 찾기
```python
filenames = os.listdir(os.path.join("./"))
filenames
'''
['.ipynb_checkpoints',
 '20190107.ipynb',
 'animals.csv',
 'animals2.csv',
 'basic.ipynb',
 'fruits.csv',
 'second.txt',
 'test.txt']
'''

# for loop
result = []
for filename in filenames:
    if filename.endswith(".txt"):
        result.append(filename)
result
# ['second.txt', 'test.txt']

# lambda
list(filter(
    lambda filename: filename.endswith(".txt"),
    filenames
))
# ['second.txt', 'test.txt']

# list comprehension
[
    filename
    for filename in filenames
    if filename.endswith(".txt")
]
# ['second.txt', 'test.txt']
```

* 폴더만들기
```python
os.makedirs("./makedirs")

```

* 파일 복사하기
```python
def copy(src_filename, dest_filename):
    with open(src_filename, "r") as src_fp
        data = src_fp.read()

        with open(dest_filename, "w") as dest_fp:
            dest_fp.write(data)
```

```python
#  src.txt 파일을 만들고, automate 에는 파일이 없는 상태다.
copy("./src.txt","./automate/dest.txt") # 복사하기 함수 실행
#또는 경로로 적어서 실행한다.
copy(os.path.join("src.txt"),(os.path.join("automate","dest.txt")))
os.listdir(os.path.join("./automate/")) # automate 폴더안의 파일 리스트 반환하기
['dest.txt']

# 이렇게 파일을 복사하게 되면 메타정보가 깨지게 되는 점 유의하자
# 따라서 이를 보완하기 위해 파일 및 폴더 관리 라이브러리는
# shutil 라이브러리를 사용하도록 한다.
```

## shutil 
* 복잡한 파일 관리
```python
import shutil
# 대부분 shutil.copy2 를 많이 사용한다.
# 파일 복사하기
shutil.copy2(os.path.join("src.txt"),os.path.join("automate","dest.txt"))
os.listdir(os.path.join("./automate/"))
# 이 방법은 파일만 복사할 수 있다.

# 폴더 복사하기
# 현재 존재하는 automate폴더를 새로 만들어진 new_automate에 복사한다.
shutil.copytree(os.path.join("automate"),os.path.join("new_automate"))
os.listdir() # 폴더가 복사되었는지 확인


# 파일 삭제하기
os.remove("./automate/dest.txt")

# 폴더 삭제하기
os.removedirs("./automate/") # 폴더안에 파일이 없어야 지울 수 있다.

shutil.rmtree("./automate/") # 폴더안에 파일이 있어도 지울 수 있다.

```

** 파일 이동하기
```python
os.rename("./new_automate/dest.txt","/new_automate/copy.txt")

shutil.move("./new_automate/copy.txt","./new_automate/move.txt")
```

* 년도 별로 사진 파일 분류하기
사진 파일 이름은 다음과 같이 동일한 포맷 갖는다고 가정
screenshot-2019-01-15.jpg
```python
if "Photos" in os.listdir(): # 현재 폴더에 "Photos"라는 폴더가 있다면
    shutil.rmtree("./Photos") # "Photos" 폴더를 삭제한다.
os.makedirs("Photos") # "Photos" 폴더를 생성한다.

filenames = os.listdir("./hello/") # "Hello" 폴더 안의 파일들을 filenames 리스트로 얻는다.

for filename in filenames: # filenames의 리스트 첫번째 부터 마지막 열까지 for loop을 돌리면서
    year = filename.split(".")[0].split("-")[1] # 년도 부분을 year라는 변수에 저장한다.
    month = filename.split(".")[0].split("-")[2] # 월 부분을 month라는 변수에 저장한다.

    if not year in os.listdir("./Photos/"): # Photos 폴더에 year에 해당하는 폴더가 없다면,
        os.makedirs("./Photos/{year}/".format(year=year)) # 그 year에 해당하는 폴더를 만든다.

    if not month in os.listdir(os.path.join(".","Photos", year)): # Photos 폴더의 해당 year 폴더 안에 month에 해당하는 폴더가 없다면,
        os.makedirs("./Photos/{year}/{month}".format(year=year, month=month)) # 그 month에 해당하는 폴더를 만든다.

    src_filename = os.path.join(".","hello",filename) # 원본 파일 경로 지정
    dest_filename = os.path.join(".","Photos",year,month,filename) # 복사본 파일 경로 지정
    shutil.copy2(src_filename, dest_filename) # 파일 복사를 시작한다.
```

