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
```

* 참고
[https://www.python-course.eu/python3_formatted_output.php](https://www.python-course.eu/python3_formatted_output.php)