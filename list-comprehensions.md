# List Comprehensions

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
    ("two" if i % 2 == 0 else "") + ("three" if i % 3 == 0 else "")
    for i
    in range(1, 20+1)
]
# 위의 코드는 가독성이 안좋으므로 다음 처럼 멀티라인으로 적는다.

[
    ("two" if i % 2 == 0 else "") +\
        ("three" if i% 3 == 0 else "")  # 인덴트 들여쓰기 해주는 것과 역슬래쉬(\)가 멀티라인의 포인트이다.
    for i
    in range(1, 20+1)
]

# ['', 'two', 'three', 'two', '', 'twothree', '', 'two', 'three', 'two', '', 'twothree', '', 'two', 'three', 'two', '', 'twothree', '', 'two']
```

