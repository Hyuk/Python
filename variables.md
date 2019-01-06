# Variables = Data Types
* Numbers
* Strings
* list = [ "element1", "element2" ]
* Set = { "element1", "element2" }
* Dict = { "key1": "value1", "key2": "value2" }
* Tuple = ( "element1", "element2" )
* Boolean = True False
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
animal = ["강아지", "고양이", "원숭이", "물고기"]
animal[0]
# 강아지
animal[-1]
# 물고기
animal[0:3]
# M:N => M ~ N-1 
# ["강아지", "고양이", "원숭이"]
animal[1:0]
# ["고양이", "원숭이", "물고기"]
animal[:2]
# ["강아지", "고양이", "원숭이"]
```

## Set (집합)
```python
animal = {"강아지", "고양이", "원숭이", "물고기"}
```

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

## Dict
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

```

### List, Set, Dist vs Tuple 
List, Set, Dist 먼저 정의한 후에 데이터를 변경 및 추가할 수 있다
Tuple은 데이터를 추가할 수 없다. 재정의를 해야한다.

## Boolean
```python
10 > 5
# True
2 > 3
# False
```
# Conditional Statement (if, elif, else)
```python
if 10 > 5:
    print("10이 5보다 크다.")
# 10이 5보다 크다.

my_num = 23
if my_num > 0:
    print(my_num + "은 양수이다.")
elif my_num == 0:
    print(my_num + "은 0이다.")
else:
    print(my_num + "은 음수이다.")

"참이다" if 10 > 5 else "거짓이다"
# '참이다'

"양수이다" if 0 > 0 else ("음수이다" if 0 < 0 else "0이다")
# '0이다'
```

# Loops Statement (for loop, do while loop)
```python
for i in range(10): # 0부터 (n-1) -> 0,1,2,3,4,5,6,7,8,9
    print(i)
#
0
1
2
3
4
5
6
7
8
9

# For loop을 사용해서 List 데이터 표시하기
animals = ["강아지", "고양이", "물고기"]
for animal in animals:
    print(animal + "을/를 키우고 있습니다.")

# 강아지을/를 키우고 있습니다.
# 고양이을/를 키우고 있습니다.
# 물고기을/를 키우고 있습니다.

# FOr loop을 사용해서 Dist 데이터 표시하기
student = student = {"name": "Hyuk", "age": "20", "email": "hyukho83@gmail.com"}
for key in student:
    value = student[key]
    # print(value)
    print(key + " => " + str(student[key]))

for key, value in student.items():
    print(key + " => " + str(value))


```