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
```