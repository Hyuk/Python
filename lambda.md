# Lambda
이름이 있는 함수; 익명함수
```python
numbers = [1,2,3,4,5]
[number**2 for number in numbers]
# [1,4,9,16,25]
```

### Converting the function to Lambda function (Single variable)
```python
def double(x):
    return x*2
double(10)
# 20
```

```python
(lambda x: 2*x)(10)
# 20
```

### Converting the function to Lambda function (List)
```python
my_list = [1,2,3,4,5]

result = []

def double(x):
    return x*2

for element in my_list:
    result.append(double(element))

result
# [2, 4, 6, 8, 10]

```
* Converting the function above with list and map function
```python
my_list = [1,2,3,4,5]
def double(x):
    return x*2
list(map(double,my_list))
# [2, 4, 6, 8, 10]
```
* Converting the function above with lambda function
```python
my_list = [1,2,3,4,5]
list(map(
    lambda x: x*2,my_list
))
# [2, 4, 6, 8, 10]
```

## Lambda 함수와 이미 존재하는 함수를 사용해서 새로운 함수를 만드는 방법
```python
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

read_lsv = lambda filepath: read_csv(filepath,"|")
# Same expression with the code below:

# def read_lsv(filepath):
#    return read_csv(filepath,"|")

read_lsv("./animals2.csv")
# [{'Korean name': '강아지', 'English name': 'dog', 'Size': '중형'},
#  {'Korean name': '고양이', 'English name': 'cat', 'Size': '소형'},
#  {'Korean name': '물고기', 'English name': 'fish', 'Size': '초소형'},
#  {'Korean name': '원숭이', 'English name': 'monkey', 'Size': '대형'}]
```

## Lambda Operator - map, filter, reduce
* map(1. 함수, 2. 리스트)
[2. 리스트]의 각각의 element에 동일한 [1 함수]를 적용해서 새로운 리스트를 반환!

* filter(1. 함수, 2. 리스트)
[2. 리스트]의 각각의 element에 동일한 [1 함수]를 적용한 다음에, 함수의 결과가 True인 Element만 남겨서 새로운 리스트 반환!
```python
list(map(lambda x:x*2,[1,2,3]))
# [2, 4, 6]

list(filter(lambda x:x>2,[1,2,3]))
# [3]
```

* 1-10 까지의 자연수 리스트 => 제곱한 결과 중에서 50이상의 수만 리스트
```python
# for 문을 이용한 방법
# my_list=[]
# for element in range(11):
#     my_list.append(element)

# new_list = []
# for element in my_list:
#     if(element**2 > 50):
#         new_list.append(element**2)
# new_list
result = []
for i in range(1, 10+1):
    element = i**2

    if element > 50:
        result.append(element)
result
# [64, 81, 100]

# lambda 문을 이용한 방법
# my_list=[]
# for element in range(11):
#     my_list.append(element)
# list(filter(
#     lambda x:x>50,list(map(
#         lambda x:x**2, my_list
#     ))
# ))
list(filter(
    lambda x: x>50,
    list(map(
        lambda x:x**2, range(1,10+1)
    ))
))
# [64, 81, 100]
```

## reduce
```python
def get_sum(my_list):
    result=0
    for element in my_list:
        result = result + element
    return result

get_sum([1,2,3,4,5])

# Reduce
# 1, 2, 3, 4, 5
#    3, 3, 4, 5
#       6, 4, 5
#         10, 5
#            15
# Reduce


```
## Reduce 를 사용하려면 라이브러리에서 불러와서 써야한다
```python
from functools import reduce
```

## Reduce와 Lambda를 사용해보자
```python
my_list = [1,2,3,4,5]
reduce(
    lambda a, b: a + b, my_list 
)
```

## input: 리스트
## output: 리스트의 element 중에서 가장 큰 수
## get_max() => filter...

## Python 2.x ( map, filter, reduce ) => python 3.X (map, filter + reduce)
## generator (map, filter => list) (generator ...)


```python
def get_max(elements):
    max = elements[0] # result = 0

    for element in elements:
        if element >= max:
            max = element
    return max

get_max([1, 100, 2, 3, 4, 105, 6])
# 105
```

```python
my_list = [1, 100, 2, 3, 105, 4]
reduce(
    lambda a, b: a if a>b else b, my_list
)
# 105
```

```python
get_max = lambda elements: reduce(
    lambda a, b:a if a>b else b, my_list
)
get_max([1, 100, 2, 3, 4, 105, 6])
# 105
```

## List Comprehension - 리스트 표현식 - 리스트를 정의하는 것 처럼 쓰지만, 실제로 내부적으로는 Lambda Operator
* Lambda 표현식
```python
list(map(
    lambda x: x**2,
    range(1,5+1)
))

# [1, 4, 9, 16, 25]
```

* List Comprehension
```python
[
    i**2
    for i
    in range(1,5+1)
]

# [1, 4, 9, 16, 25]
```

```python
[
    i
    for i 
    in [101, 2, 3, 104, 105]
]

# [101, 2, 3, 104, 105]
```

```python
[
    i
    for i 
    in [101, 2, 3, 104, 105]
    if i > 100
]

# [101, 104, 105]
```

```python
[
    i**2
    for i
    in range(1, 10+1)
    if i**2 >= 50
]

# [64, 81, 100]

# 한줄로 표현 하는 것도 가능하다
[i**2 for i in range(1, 10+1) if i**2 >=50]
# [64, 81, 100]
```

## List Comprehension을 사용해서 파일 읽기
```python
'''
fruits.csv
사과,Apple,중형
딸기,Strawberry,소형
포도,grape,중형
'''
[
    row
    for row
    in open("./fruits.csv","r",encoding="UTF-8").read().split("\n")
]
# ['사과,Apple,중형', '딸기,Strawberry,소형', '포도,grape,중형']


[
    {
        "Korean Name": row.split(",")[0],
        "Eng Name": row.split(",")[1],
        "Size": row.split(",")[2],
    }
    for row
    in open("./fruits.csv","r",encoding="UTF-8").read().split("\n")
]

# [{'Korean Name': '사과', 'Eng Name': 'Apple', 'Size': '중형'},
#  {'Korean Name': '딸기', 'Eng Name': 'Strawberry', 'Size': '소형'},
#  {'Korean Name': '포도', 'Eng Name': 'grape', 'Size': '중형'}]
```

## 소수(Prime Numbers) 구하기
```python
[
    i
    for i
    in range(1, 100+1)
    if all(
        i % j != 0
        for j
        in range(2, i)
    )
]
# [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

## 리스트에서 2의 배수 문자표현 그리고 나머지 빈칸
```python
[
    "TWO" if (i+1)%2 == 0 else ""
    for i
    in range(10)
]

# ['', 'TWO', '', 'TWO', '', 'TWO', '', 'TWO', '', 'TWO']
```

##  리스트에서 3의 배수 문자표현 그리고 나머지 빈칸
```python
[
    "Three" if (i+1)%3 == 0 else ""
    for i
    in range(10)
]

# ['', '', 'Three', '', '', 'Three', '', '', 'Three', '']
```

## 리스트에서 2의 배수 문자표현 및 3의 배수 문자표현과 그리고 나머지 빈칸
```python
[
    "TwoThree" if (i+1)%2 == 0 && (i+1)%3 == 0 else "TWO" if (i+1)%2 == 0 else "Three" if (i+1)%3 == 0 else ""
    for i
    in range(10)
]
```