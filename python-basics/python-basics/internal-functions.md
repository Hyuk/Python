# 내장함수 ( Internal Functions )
* [print() - 프린트 함수](#print)
* [float() - 정수를 실수로 변환하는 함수](#float)
* [int() - 실수를 정수로 변환하는 함수](#int)
* [input() - 사용자로 부터 문자열을 입력 받는 함수](#input)


## print()
* 프린트 함수
```python
num1 = 24
print(num1)
# 24
```

* 여러개의 프린트 함수를 쓸때 한줄로 표현하는 방법
```python
print("Hello World!", end = ' ')
print("My name is Hyuk")
# Hello World! My name is Hyuk
```

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

## input()
* 사용자로 부터 문자열을 입력받는다
```python
saysomething1 = input()
# hello world
saysomething1
# hello world
```
