# file management

## 파일 읽기
open(), read(), close()
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
fp.close()
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

## with
with와 함께 open 문을 실행하면 close가 필요없이 블락이 끝나면 자동으로 닫힌다.
```python 
with open("./animals.csv") as fp:
    data = fp.read()
data
```

## CSV File Manipulation
```python
fp = open("./animals.csv","r",encoding="UTF-8")
data = fp.read()
data
# '강아지,dog\n고양이,cat\n물고기,fish\n원숭이,monkey'

data.split("\n")
# ['강아지,dog', '고양이,cat', '물고기,fish', '원숭이,monkey']
```

* read() // 여러줄을 \n 표시 포함해서 한줄로 표시한다 - 문서 전체가 String 형태로 return
* readline() // 여러줄 중 순서대로 한줄씩 읽는다 - 한 줄 ( newline character를 기준으로 끊어서 가져오는 기능 )
* readlines() // 여러줄을 List 형태로 반환한다. - 전체를 newline character를 기준으로 나눠서 List return
```python
fp = open("./animals.csv","r",encoding="UTF-8")
data = fp.readline()
data
# '강아지,dog\n'
```

```python
fp = open("./animals.csv","r",encoding="UTF-8")
data = fp.readlines()
data
# ['강아지,dog\n', '고양이,cat\n', '물고기,fish\n', '원숭이,monkey']
```
```python
with open("./animals.csv",encoding="UTF-8") as fp:
    data = fp.read()
    print(data)

# 강아지,dog
# 고양이,cat
# 물고기,fish
# 원숭이,monkey

with open("./animals.csv",encoding="UTF-8") as fp:
    data = fp.read()

data

# '강아지,dog\n고양이,cat\n물고기,fish\n원숭이,monkey'

with open("./animals.csv",encoding="UTF-8") as fp:
    data1 = fp.readline()
    data2 = fp.readline()

data1
data2

# '고양이,cat\n'

with open("./animals.csv",encoding="UTF-8") as fp:
    data = fp.readlines() # 불필요한 \n은 반드시 지워줘야 한다.

data

# ['강아지,dog\n', '고양이,cat\n', '물고기,fish\n', '원숭이,monkey']
```


```python
with open("./animals.csv",encoding="UTF-8") as fp:
    data = fp.read()
    rows = data.split("\n")

rows
# ['강아지,dog', '고양이,cat', '물고기,fish', '원숭이,monkey']
```

```python
with open("./animals.csv",encoding="UTF-8") as fp:
    result = [] # 빈 리스트 생성
    
    data = fp.read() 
    rows = data.split("\n")

    for row in rows:
        animal = {
            "Korean Name": row.split(",")[0],
            "English Name": row.split(",")[1],
        }

        result.append(animal)

result
# [{'Korean Name': '강아지', 'English Name': 'dog'},
# {'Korean Name': '고양이', 'English Name': 'cat'},
# {'Korean Name': '물고기', 'English Name': 'fish'},
# {'Korean Name': '원숭이', 'English Name': 'monkey'}]
```

## using pandas to display

```python
with open("./animals.csv",encoding="UTF-8") as fp:
    result = [] # 빈 리스트 생성
    
    data = fp.read() 
    rows = data.split("\n")

    for row in rows:
        animal = {
            "Korean Name": row.split(",")[0],
            "English Name": row.split(",")[1],
        }

        result.append(animal)

result

import pandas as pd
pd.DataFrame(result)


```

## Jupyter Notebook에서 Pandas Library를 Import하지 못할때
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

## Read CSV file and make a list of dict
```python
'''
animals.csv

Korean name,English name,Size
강아지,dog,중형
고양이,cat,소형
물고기,fish,초소형
원숭이,monkey,대형
'''

with open("./animals.csv",encoding="UTF-8") as fp:
    result = [] # 빈 리스트 생성
    
    rows = fp.read().split("\n")
    # 1. Column 을 따로 다루는 코드
    column = rwos[0].split(",")

    # 2. 실제 데이터를 따로 다루는 코드
    for row in rows[1:]:
        row_datas = row.split(",")
        row_dict = {}

        # Column을 for 문 돌리면서 
        # Column에 적절한 데이터를 추가한다. ( "Korean Name" =  "강아지", "Size => "중형" )
        for column_index in range(len(column)):
            column = columns[column_index]
            row_dict[column] = row_datas[column_index]
        result.append(row_dict)

result

```


