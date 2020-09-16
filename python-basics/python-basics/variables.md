# Variables = Data Types
* Numbers (숫자)
* Strings (문자)
* List = [ "element1", "element2" ] (리스트)
* Set = { "element1", "element2" } (세트)
* Dict = { "key1": "value1", "key2": "value2" } (딕셔너리)
* Tuple = ( "element1", "element2" ) (튜플)
* Boolean = True False (불린)
* Functions (함수)

## Variables
* Basic Usage of Variable
```python
name = "Hyuk" # Assign a value to the variable

"Hello, " + name # concatenate with the plus sign

# Hello, Hyuk

type(name) # check the type of the value

# str
```

* Variables are case sensitive
```python
NAME = "Obama"
name = "Trump"

name

# 'Trump'

NAME

# 'Obama'
```

* Multiline String
```python
multiline = 
'''
welcome to 
the python school
'''
multiline
# 'welcome to \nthe python school\n'
```

## Numbers (숫자)
```python
1000 # 정수형 데이터
1000.0 # 실수형 데이터
```

## Strings (문자)
```python
"Hyuk" # 문자형 데이터
"Hello" + ", Hyuk" # "+" 기호를 사용해서 Concatenate 기능을 사용할 수 있다.
# Hello, Hyuk
```
* Multiline String
```python
email1 = """
Dear Hyuk

Hello World

Best Regards,
Hugo
"""
print(email1)
```

## List
```python
animal = ["Dog", "Cat", "Monkey", "Fish"]
animal[0]
# Dog
animal[-1]
# Fish
animal[0:3]
# M:N => M ~ N-1 
# ["Dog", "Cat", "Monkey"]
animal[1:0]
# ["Cat", "Monkey", "Fish"]
animal[:2]
# ["Dog", "Cat", "Monkey"]
```

## Set (집합)
```python
animal = {"Dog", "Cat", "Monkey", "Fish"}
```

### List와 Set 비교 및 다른점
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

### List의 각 값을 대문자로 변환하는 방법
```python
fruits = ['Banana', 'Apple', 'Lime']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)
# ['BANANA', 'APPLE', 'LIME']

```

### List와 enumerate함수 // List의 각 인덱스 값과 List Value를 Tuple형태로 업데이트 한다
```python
fruits = ['Banana', 'Apple', 'Lime'].
list(enumerate(fruits))
[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]
```

## Dict (Dictionary)
Dict = { "key1": "value1", "key2": "value2" }
```python
student = {"name": "Hyuk", "age": "20", "email": "hyukho83@gmail.com"}
student
# {'name': 'Hyuk', 'age': '20', 'email': 'hyukho83@gmail.com'}
```

### Dict에 데이터 추가하기
```python
student = {"name": "Hyuk", "age": "20", "email": "hyukho83@gmail.com"}
student["address"] = "주소"
student
# {'name': 'Hyuk', 'age': '20', 'email': 'hyukho83@gmail.com', 'address': '주소'}
```

## Tuple
Tuple = ( "element1", "element2" )
```python
animal = ( "dog", "cat" )
```

### List, Set, Dict vs Tuple 
List, Set, Dist 먼저 정의한 후에 데이터를 변경 및 추가할 수 있다
Tuple은 데이터를 추가할 수 없다. 재정의를 해야한다.

## Boolean
```python
10 > 5
# True
2 > 3
# False
```

