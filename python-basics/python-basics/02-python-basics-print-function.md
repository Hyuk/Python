# Python Basics (파이썬 기초)

### Print Function
* Single Line & Multi Line
```python
print('Hello World') # Single Line
print("Hello world") # Single Line
print('''Hello World''') # Multi Line
print("""Hello world""") # Multi Line

# Hello World
```

* sep (separator)옵션 사용
```python
print('T', 'E', 'S', 'T')
# T E S T

print('T', 'E', 'S', 'T', sep='')
# TEST

print('2021', '05', '03', sep='-')
# 2021-05-03

print('niceman','google.com', sep='@')
# niceman@google.com
```

* end 옵션 사용
```python
print('Welcome To', end='')
print('the black parade', end='')
# Welcome Tothe black parade

print('Welcome To', end='')
print(' the black parade', end='')
print(' piano notes')
# Welcome To the black parade piano notes

print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
# Welcome To the black parade piano notes
```

* format 옵션 사용
```python
print('{} and {}'.format('You', 'Me'))
# You and Me

print('{0} and {1} and {0}'.format('You', 'Me'))
# You and Me and You

print('{} and {}'.format(a='You', b='Me'))
# You and Me
```

* % 옵션 사용
```python
print("%s's favorite number is %d" % ('Eunki', 7)) # %s: 문자, %d: 정수, %f: 실수
# Eunki's favorite number is 7

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
# Test1:   776, Price: 6534.12

print("Test1: {0: 5d}, Price: {1: 4.2f}".format(24, 654.2345))
# Test1:    24, Price:  654.23

print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=235, b=289.32089))
# Test1:   235, Price:  289.32
```

* 참고
[https://www.python-course.eu/python3_formatted_output.php](https://www.python-course.eu/python3_formatted_output.php)

### Escape 코드
| Escape 코드 | 뜻 |
| ----- | -----|
| \n | 개행 |
| \t | 탭 |
| \\ | 문자 |
| \' | 문자 |
| \" | 문자 |
| \r | 캐리지 리턴 |
| \f | 폼 피드 |
| \a | 벨 소리 |
| \b | 백 스페이스 |
| \000 | 널 문자 |

### 입력과 출력
```python
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# utf-8
# utf-8
```