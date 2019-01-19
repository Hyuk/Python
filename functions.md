# 함수 ( Functions )
* [float() - 정수를 실수로 변환하는 함수](#float)
* int() - 실수를 정수로 변환하는 함수
* input() - 사용자로 부터 문자열을 입력 받는 함수

## float()
* 정수를 실수로 변환하는 함수
```python
num1 = 24
num2 = float(num1)
num2
# 24.0
```

## int()
* 실수를 정수로 변환하는 함수
```python
num1 = 24.7
num2 = int(num1)
num2
# 24
```

* 숫자로 된 문자는 정수 또는 실수로 변환할 수 있다.
* 실수로 된 문자는 실수로, 정수로 된 문자는 정수로 변환한다.
```python
string1 = "24.7"
num2 = float(string1)
num2
# 24.7

string1 = "24"
num2 = int(string1)
num2
# 24
```

## 기본적인 함수 선언 및 호출
```python
def greeting():
    print("Hello World")

greeting()
# Hello World

def greeting(name):
    print(name + "님, 안녕하세요.")

greeting("Hyuk")
# Hyuk님, 안녕하세요.
```

## 조건문이 들어간 기본 함수
```python
def check_number(my_number):
    if (my_number > 0):
        print("Number is greater than 0.")
    elif (my_number < 0):
        print("Number is less than 0.")
    else:
        print("Number is equal to 0.")

check_number(0)
# Number is equal to 0.
```
## 함수에서 print와 return의 차이
return을 쓰도록 한다.
```python
def check_number(my_number):
    if (my_number > 0):
        return "Number is greater than 0."
    elif (my_number < 0):
        return "Number is less than 0."
    else:
        return "Number is equal to 0."

result = check_number(0)
result
# 'Number is equal to 0.'
```

## String과 관련된 함수들
* split
* join
* replace
* startswith
* endswith

### split
String을 Seperator를 기준으로 나누고 List 형태로 반환한다.
```python
data = "123,hello,world,78,pass"
data.split(",")
# ['123', 'hello', 'world', '78', 'pass']
```

### join
```python
data2 = ['123', 'hello', 'world']
"-".join(data2)
# '123-hello-world'
```

### split <=> join

### replace
```python
data = "123,hello,world,78,pass"
data.replace(",","|")
# '123|hello|world|78|pass'
```

### in
check the string has the letters inside
```python
data = "123,hello,world,78,pass"
"ello" in data
# True
```

### startswith
```python
data = "123,hello,world,78,pass"
data.startswith("12")
# True
```

### endswith
```python
data = "123,hello,world,78,pass"
data.endswith("ass")
# True
```

## List 관련 함수들
* append

### append
List에 새로운 데이터를 추가할 때
```python
animals = []
animals.append("dog")
animals
# ['dog']
animals.append("cat")
animals
# ['dog', 'cat']
```

## Dict 관련 함수들
* get

### get
학생 1000명을 for 문 돌다가, address 가 있으면 address를 출력하고, 없으면 "주소 없음" 이라고 출력하자.
```python
student = {"name": "Hyuk", "email": "email@email.com"}
student["name"]
# Hyuk
student.get("address","주소 없음")
# 주소 없음
```