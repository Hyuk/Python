# File I/O - CSV File

## CSV : MIME - text/csv

## CSV
* CSV 파일 읽기
```python
import csv

with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    # next(reader) # 첫번째 행 Header 를 제외하고 가져온다.
    #확인
    print(reader)
# <_csv.reader object at 0x000002BAE6F9D460>
    print(type(reader))
# <class '_csv.reader'>

    print(dir(reader)) # __iter__ 가 있으므로 for loop을 돌릴 수 있다.

# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dialect', 'line_num']

    print()
    for c in reader:
        print(c)

# ['번호', '이름', '가입일시', '나이']
# ['1', '김정수', '2017-01-19 11:30:00', '25']
# ['2', '박민구', '2017-02-07 10:22:00', '35']
# ['3', '정순미', '2017-01-22 09:10:00', '33']
# ['4', '김정현', '2017-02-22 14:09:00', '45']
# ['5', '홍미진', '2017-04-01 18:00:00', '17']
# ['6', '김순철', '2017-05-14 22:33:07', '22']
# ['7', '이동철', '2017-03-01 23:44:45', '27']
# ['8', '박지숙', '2017-01-11 06:04:18', '30']
# ['9', '김은미', '2017-02-08 07:44:33', '51']
# ['10', '장혁철', '2017-12-01 13:01:11', '16']
```

* CSV 파일이 ',' 가 아닌 다른 '|' 기호로 구분되어 있을때,
```python
import csv

with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f, delimiter='|')
    for c in reader:
        print(c)

# ['번호', '이름', '가입일시', '나이']
# ['1', '김정수', '2017-01-19 11:30:00', '25']
# ['2', '박민구', '2017-02-07 10:22:00', '35']
# ['3', '정순미', '2017-01-22 09:10:00', '33']
# ['4', '김정현', '2017-02-22 14:09:00', '45']
# ['5', '홍미진', '2017-04-01 18:00:00', '17']
# ['6', '김순철', '2017-05-14 22:33:07', '22']
# ['7', '이동철', '2017-03-01 23:44:45', '27']
# ['8', '박지숙', '2017-01-11 06:04:18', '30']
# ['9', '김은미', '2017-02-08 07:44:33', '51']
# ['10', '장혁철', '2017-12-01 13:01:11', '16']
```

* Dict 변환
```python
import csv

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('---------------')

# 번호 1
# 이름 김정수
# 가입일시 2017-01-19 11:30:00
# 나이 25
# ---------------
# 번호 2
# 이름 박민구
# 가입일시 2017-02-07 10:22:00
# 나이 35
# ---------------
# 번호 3
# 이름 정순미
# 가입일시 2017-01-22 09:10:00
# 나이 33
# ---------------
# 번호 4
# 이름 김정현
# 가입일시 2017-02-22 14:09:00
# 나이 45
# ---------------
# 번호 5
# 이름 홍미진
# 가입일시 2017-04-01 18:00:00
# 나이 17
# ---------------
# 번호 6
# 이름 김순철
# 가입일시 2017-05-14 22:33:07
# 나이 22
# ---------------
# 번호 7
# 이름 이동철
# 가입일시 2017-03-01 23:44:45
# 나이 27
# ---------------
# 번호 8
# 이름 박지숙
# 가입일시 2017-01-11 06:04:18
# 나이 30
# ---------------
# 번호 9
# 이름 김은미
# 가입일시 2017-02-08 07:44:33
# 나이 51
# ---------------
# 번호 10
# 이름 장혁철
# 가입일시 2017-12-01 13:01:11
# 나이 16
# ---------------
```

* 리스트를 CSV파일로 쓰는 방법 with for loop
```python
import csv

w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)
```

* 리스트를 CSV파일로 쓰는 방법 without for loop
```python
import csv

w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)
```

# 
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
    columns = rows[0].split(",")

    # 2. 실제 데이터를 따로 다루는 코드
    for row in rows[1:]:
        row_datas = row.split(",")
        row_dict = {}

        # Column을 for 문 돌리면서 
        # Column에 적절한 데이터를 추가한다. ( "Korean Name" =  "강아지", "Size => "중형" )
        for column_index in range(len(columns)):
            column = columns[column_index]
            row_dict[column] = row_datas[column_index]
        result.append(row_dict)

result
# [{'Korean name': '강아지', 'English name': 'dog', 'Size': '중형'},
#  {'Korean name': '고양이', 'English name': 'cat', 'Size': '소형'},
#  {'Korean name': '물고기', 'English name': 'fish', 'Size': '초소형'},
#  {'Korean name': '원숭이', 'English name': 'monkey', 'Size': '대형'}]
```


## 함수선언을 사용해서 파일 읽고 리턴하기

```python
'''
animals.csv

Korean name,English name,Size
강아지,dog,중형
고양이,cat,소형
물고기,fish,초소형
원숭이,monkey,대형
'''
def read_csv(filepath):
    with open(filepath,encoding="UTF-8") as fp:
        result = [] # 빈 리스트 생성

        rows = fp.read().split("\n")
        # 1. Column 을 따로 다루는 코드
        columns = rows[0].split(",")

        # 2. 실제 데이터를 따로 다루는 코드
        for row in rows[1:]:
            row_datas = row.split(",")
            row_dict = {}

            # Column을 for 문 돌리면서 
            # Column에 적절한 데이터를 추가한다. ( "Korean Name" =  "강아지", "Size => "중형" )
            for column_index in range(len(columns)):
                column = columns[column_index]
                row_dict[column] = row_datas[column_index]
            result.append(row_dict)

    return result

read_csv("./animals.csv")
# [{'Korean name': '강아지', 'English name': 'dog', 'Size': '중형'},
#  {'Korean name': '고양이', 'English name': 'cat', 'Size': '소형'},
#  {'Korean name': '물고기', 'English name': 'fish', 'Size': '초소형'},
#  {'Korean name': '원숭이', 'English name': 'monkey', 'Size': '대형'}]
```

## Seperator가 다른 파일을 읽는 경우 (tab => tsv, "/", "|" etc)
```python

'''
animals.csv

Korean name,English name,Size
강아지,dog,중형
고양이,cat,소형
물고기,fish,초소형
원숭이,monkey,대형
'''
'''
animals2.csv

Korean name|English name|Size
강아지|dog|중형
고양이|cat|소형
물고기|fish|초소형
원숭이|monkey|대형
'''
def read_csv(filepath, seperator=","):
    with open(filepath,encoding="UTF-8") as fp:
        result = [] # 빈 리스트 생성

        rows = fp.read().split("\n")
        # 1. Column 을 따로 다루는 코드
        columns = rows[0].split(seperator)

        # 2. 실제 데이터를 따로 다루는 코드
        for row in rows[1:]:
            row_datas = row.split(seperator)
            row_dict = {}

            # Column을 for 문 돌리면서 
            # Column에 적절한 데이터를 추가한다. ( "Korean Name" =  "강아지", "Size => "중형" )
            for column_index in range(len(columns)):
                column = columns[column_index]
                row_dict[column] = row_datas[column_index]
            result.append(row_dict)

    return result
read_csv("./animals.csv")
# [{'Korean name': '강아지', 'English name': 'dog', 'Size': '중형'},
#  {'Korean name': '고양이', 'English name': 'cat', 'Size': '소형'},
#  {'Korean name': '물고기', 'English name': 'fish', 'Size': '초소형'},
#  {'Korean name': '원숭이', 'English name': 'monkey', 'Size': '대형'}]

def read_csv(filepath, seperator=","):
    with open(filepath,encoding="UTF-8") as fp:
        result = [] # 빈 리스트 생성

        rows = fp.read().split("\n")
        # 1. Column 을 따로 다루는 코드
        columns = rows[0].split(seperator)

        # 2. 실제 데이터를 따로 다루는 코드
        for row in rows[1:]:
            row_datas = row.split(seperator)
            row_dict = {}

            # Column을 for 문 돌리면서 
            # Column에 적절한 데이터를 추가한다. ( "Korean Name" =  "강아지", "Size => "중형" )
            for column_index in range(len(columns)):
                column = columns[column_index]
                row_dict[column] = row_datas[column_index]
            result.append(row_dict)

    return result

read_csv("./animals2.csv","|")
# [{'Korean name': '강아지', 'English name': 'dog', 'Size': '중형'},
#  {'Korean name': '고양이', 'English name': 'cat', 'Size': '소형'},
#  {'Korean name': '물고기', 'English name': 'fish', 'Size': '초소형'},
#  {'Korean name': '원숭이', 'English name': 'monkey', 'Size': '대형'}]

```