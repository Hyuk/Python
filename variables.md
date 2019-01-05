# Variables = Data Types
* Numbers
* Strings
* list = [ ]
* Set = { }
* Dict = { "key1": "value1", "key2": "value2" }
* Functions

## NUmbers
```python
1000 # 정수형 데이터
1000.0 # 실수형 데이터
```

## Strings
```python
"Hyuk" # 문자형 데이터
"Hello" + ", Hyuk" 
# Hello, Hyuk
```

## Variables
```python
name = "Hyuk" # Assign a value to the variable
"Hello, " + name # concatenate with the plus sign
# Hello, Hyuk
type(name) # check the type of the value
# str
```

## List
```python
animal = ["원숭이", "고양이", "원숭이", "물고기"]
animal[0]
# 원숭이
animal[-1]
# 물고기
animal[0:3]
# M:N => M ~ N-1 
# ["원숭이", "고양이", "원숭이"]
animal[1:0]
# ["고양이", "원숭이", "물고기"]
animal[:2]
# ["원숭이", "고양이", "원숭이"]
```

## Set (집합)

### List 와 Set 비교 및 다른점
* List
여러 Elements 들을 저장하고 있는 자료형 (Element 하나하나는 어떤 자료형 상관 x)
중복 o, 순서 o

* Set
여러 Elements 들을 저장하고 있는 자료형
중복 x, 순서 x

### List 를 Set으로 변경
```python
animals = ["dog", "dog", "dog", "cat"] #List
set(animals)
# {'cat', 'dog'}
```

### List의 중복된 값들을 제거하는 방법
```python
my_List = ["A","A","B","C","C","C","D","D","D","D"]
list(set(my_List)) #set으로 한번 변경한 뒤에 list로 변환
# ['C', 'A', 'B', 'D']
```

# Conditional Statement (if else, switch)
```python
1+3
# 4
```

# Loops Statement (for loop, do while loop)
```python

```